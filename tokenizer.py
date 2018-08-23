import csv
from datetime import datetime
from nltk.tokenize.moses import MosesTokenizer, MosesDetokenizer


if __name__ == '__main__':
	path = 'data/main/'
	path1 = 'CSV/0.0/'
	path2 = 'CSV/1.0/'

	with open(path1 + 'train.from', 'r') as train1_0_from,\
	open(path1 + 'train.to', 'r') as train1_0_to,\
	open(path2 + 'train.from', 'r') as train2_0_from,\
	open(path2 + 'train.to', 'r') as train2_0_to,\
	open(path + 'train.from', 'a', encoding='utf-8') as train_from,\
	open(path + 'train.to', 'a', encoding='utf-8') as train_to,\
	open(path + 'test1.from', 'a', encoding='utf-8') as test1_from,\
	open(path + 'test1.to', 'a', encoding='utf-8') as test1_to,\
	open(path + 'test2.from', 'a', encoding='utf-8') as test2_from,\
	open(path + 'test2.to', 'a', encoding='utf-8') as test2_to,\
	open(path + 'vocab.from', 'a', encoding='utf-8') as vocab_1,\
	open(path + 'vocab.to', 'a', encoding='utf-8') as vocab_2:
		row_count1 = 0		#for 'from' files
		row_count2 = 0		#for 'to' files
		t, d = MosesTokenizer(), MosesDetokenizer()
		vocab1 = {}
		vocab2 = {}

		for line in train1_0_from:
			tokens = t.tokenize(line)
			
			for token in tokens:
				vocab1[token] = vocab1.get(token, 0) + 1

			new_line = ' '.join(str(x) for x in tokens)

			if (row_count1 % 100) == 0:
				print('original: ' + line)
				print('tokenized: ' + new_line)
				print(row_count1)

			if (row_count1 % 100) < 70:
				train_from.write(new_line)
			elif (row_count1 % 100) < 85:
				test1_from.write(new_line)
			else:
				test2_from.write(new_line)

			row_count1 += 1

		for line in train2_0_from:
			tokens = t.tokenize(line)
			
			for token in tokens:
				vocab1[token] = vocab1.get(token, 0) + 1

			new_line = ' '.join(str(x) for x in tokens)

			if (row_count1 % 100) == 0:
				print('original: ' + line)
				print('tokenized: ' + new_line)
				print(row_count1)

			if (row_count1 % 100) < 70:
				train_from.write(new_line)
			elif (row_count1 % 100) < 85:
				test1_from.write(new_line)
			else:
				test2_from.write(new_line)

			row_count1 += 1

		for line in train1_0_to:
			tokens = t.tokenize(line)
			
			for token in tokens:
				vocab2[token] = vocab2.get(token, 0) + 1

			new_line = ' '.join(str(x) for x in tokens)

			if (row_count2 % 100) == 0:
				print('original: ' + line)
				print('tokenized: ' + new_line)
				print(row_count2)

			if (row_count2 % 100) < 70:
				train_to.write(new_line)
			elif (row_count2 % 100) < 85:
				test1_to.write(new_line)
			else:
				test2_to.write(new_line)

			row_count2 += 1

		for line in train2_0_to:
			tokens = t.tokenize(line)
			
			for token in tokens:
				vocab2[token] = vocab2.get(token, 0) + 1

			new_line = ' '.join(str(x) for x in tokens)

			if (row_count2 % 100) == 0:
				print('original: ' + line)
				print('tokenized: ' + new_line)
				print(row_count2)

			if (row_count2 % 100) < 70:
				train_to.write(new_line)
			elif (row_count2 % 100) < 85:
				test1_to.write(new_line)
			else:
				test2_to.write(new_line)

			row_count2 += 1

		vocab_1.write('<unk>')
		vocab_1.write('<s>')
		vocab_1.write('</s>')

		vocab_2.write('<unk>')
		vocab_2.write('<s>')
		vocab_2.write('</s>')

		count1 = 0
		count2 = 0
		limit = 100000

		for word in sorted(vocab1.items(), key=lambda x:x[1], reverse=True):
			vocab_1.write(word[0])
			count1 += 1
			if count1 >= limit:
				break

		for word in sorted(vocab2.items(), key=lambda x:x[1], reverse=True):
			vocab_2.write(word[0])
			count2 += 1
			if count2 >= limit:
				break

