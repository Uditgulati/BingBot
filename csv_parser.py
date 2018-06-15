import csv
from datetime import datetime
import sqlite3



def acceptable(comment):
	if len(comment.split(' ')) > 100 or len(comment) == 0:
		return False
	elif len(comment) > 1000:
		return False
	elif comment == '[deleted]' or comment == '[removed]':
		return False
	else:
		return True


def main():
	filename = 'sarc'
	path = 'CSV/0.0/'

	sql_tansaction = []
	connection = sqlite3.connect('{}{}.db'.format(path, filename))
	c = connection.cursor()

	c.execute("""CREATE TABLE IF NOT EXISTS parent_reply 
		(comment_id TEXT PRIMARY KEY, comment TEXT, parent TEXT, subreddit TEXT,
		score INT)""")

	with open(path + filename + '.csv', 'r') as file:
		row_count = 0
		for line in file:
			values = [x for x in line.strip().split('	')]
			comment = values[1]
			author = values[2]
			subreddit = values[3]
			score = int(values[4])
			ups = int(values[5])
			downs = int(values[6])
			date_created = values[7]
			comment_id = str(row_count)
			parent = values[9]

			comment = comment.replace('"', "'")
			parent = parent.replace('"', "'")

			if score <= 0 or acceptable(comment) == False:
				continue

			try:
				sql = """INSERT into parent_reply (comment_id, comment, parent, 
					subreddit, score) 
					VALUES ("{}","{}","{}","{}",{});"""\
					.format(comment_id, comment, parent, subreddit, score)
				sql_tansaction.append(sql)
			except Exception as e:
				print('{' + comment + '} insert failed with exception ' + str(e))

			if len(sql_tansaction) > 10000:
				c.execute('BEGIN TRANSACTION')
				for insert in sql_tansaction:
					try:
						c.execute(insert)
					except Exception as e:
						print(str(e))
				connection.commit()
				sql_tansaction = []

			if row_count % 100000 == 0:
				print("Total row: {}, Time: {}".format(row_count, str(datetime.now())))

			row_count += 1
			#if row_count == 200000:
			#	break

if __name__ == '__main__':
	main()