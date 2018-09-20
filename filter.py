import os


if __name__ == '__main__':
	path = 'data/main/'
	path1 = 'data/small/'

	words = set()

	with open(path + 'vocab.from', 'r') as vocab:
		for line in vocab:
			words.add(line)

	with open(path + 'vocab.to', 'r') as vocab:
		for line in vocab:
			words.add(line)
	
	with open(path + 'train_1.from', 'r') as train_1from,\
	open(path + 'train_1.to', 'r') as train_1to,\
	open(path + 'train.from', 'a', encoding='utf-8') as trainfrom,\
	open(path + 'train.to', 'a', encoding='utf-8') as trainto,\
	open(path1 + 'train.from', 'a', encoding='utf-8') as small_from,\
	open(path1 + 'train.to', 'a', encoding='utf-8') as small_to:
		row_count = 0
		for line1, line2 in zip(train_1from, train_1to):
			curr_words1 = [x for x in line1.split(' ')]
			curr_words2 = [x for x in line2.split(' ')]
			if len(curr_words1) > 30 or len(curr_words2) > 30\
			or len(curr_words1) + len(curr_words2) < 6:
				continue
			c1 = 0	#no of <unk>s in sentence
			for word in curr_words1:
				if word not in words:
					c1 += 1
			for word in curr_words2:
				if word not in words:
					c1 += 1
			if c1 > 4:
				continue
			trainfrom.write(line1)
			trainto.write(line2)
			if row_count % 10 == 0:
				small_from.write(line1)
				small_to.write(line2)
			if row_count % 10000 == 0:
				print(row_count)
				print(line1, line2)
			row_count += 1

	with open(path + 'test1_1.from', 'r') as test1_1from,\
	open(path + 'test1_1.to', 'r') as test1_1to,\
	open(path + 'test1.from', 'a', encoding='utf-8') as test1from,\
	open(path + 'test1.to', 'a', encoding='utf-8') as test1to:
		row_count = 0
		for line1, line2 in zip(test1_1from, test1_1to):
			curr_words1 = [x for x in line1.split(' ')]
			curr_words2 = [x for x in line2.split(' ')]
			if len(curr_words1) > 30 or len(curr_words2) > 30\
			or len(curr_words1) + len(curr_words2) < 6:
				continue
			c1 = 0	#no of <unk>s in sentence
			for word in curr_words1:
				if word not in words:
					c1 += 1
			for word in curr_words2:
				if word not in words:
					c1 += 1
			if c1 > 4:
				continue
			test1from.write(line1)
			test1to.write(line2)
			if row_count % 10000 == 0:
				print('test1')
				print(row_count)
			row_count += 1

	with open(path + 'test2_1.from', 'r') as test2_1from,\
	open(path + 'test2_1.to', 'r') as test2_1to,\
	open(path + 'test2.from', 'a', encoding='utf-8') as test2from,\
	open(path + 'test2.to', 'a', encoding='utf-8') as test2to:
		row_count = 0
		for line1, line2 in zip(test2_1from, test2_1to):
			curr_words1 = [x for x in line1.split(' ')]
			curr_words2 = [x for x in line2.split(' ')]
			if len(curr_words1) > 30 or len(curr_words2) > 30\
			or len(curr_words1) + len(curr_words2) < 6:
				continue
			c1 = 0	#no of <unk>s in sentence
			for word in curr_words1:
				if word not in words:
					c1 += 1
			for word in curr_words2:
				if word not in words:
					c1 += 1
			if c1 > 4:
				continue
			test2from.write(line1)
			test2to.write(line2)
			if row_count % 10000 == 0:
				print('test2')
				print(row_count)
			row_count += 1