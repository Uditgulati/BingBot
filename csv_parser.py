import csv
from datetime import datetime



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

	with open(path + filename + '.csv', 'r') as file,\
	open(path + 'test.from', 'a', encoding='utf8') as test_from,\
	open(path + 'test.to', 'a', encoding='utf8') as test_to,\
	open(path + 'train.from', 'a', encoding='utf8') as train_from,\
	open(path + 'train.to', 'a', encoding='utf8') as train_to:
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

			if score <= 1 or acceptable(comment) == False:
				continue

			try:
				if row_count < 5000:
					test_from.write(parent+'\n')
					test_to.write(comment+'\n')
				train_from.write(parent+'\n')
				train_to.write(comment+'\n')
			except Exception as e:
				print('{' + comment + '} write failed with exception ' + str(e))

			if row_count % 100000 == 0:
				print("Total row: {}, Time: {}".format(row_count, str(datetime.now())))

			row_count += 1
			#if row_count == 200000:
			#	break

if __name__ == '__main__':
	main()