import os


if __name__ == '__main__':
	path = 'data/main/'

	cuss_words = ['Shit', 'Fuck', 'Bitch', 'Dick', 'Cock', 'Pussy'\
	'Asshole', 'Fag', 'Bastard', 'Slut', 'Douche']
	
	with open(path + 'vocab_1.from', 'r') as vocab_1from,\
	open(path + 'vocab_1.to', 'r') as vocab_1to,\
	open(path + 'vocab.from', 'a', encoding='utf-8') as vocabfrom,\
	open(path + 'vocab.to', 'a', encoding='utf-8') as vocabto:
		row_count1 = 0
		for line in vocab_1from:
			flag = 0
			for word in cuss_words:
				if word in line or word.upper() in line or word.lower() in line:
					flag = 1
					break
			if flag == 1:
				continue
			vocabfrom.write(line + '\n')
			row_count1 += 1

		row_count2 = 0
		for line in vocab_1to:
			flag = 0
			for word in cuss_words:
				if word in line or word.upper() in line or word.lower() in line:
					flag = 1
					break
			if flag == 1:
				continue
			vocabto.write(line + '\n')
			row_count2 += 1

		print(str(row_count1))
		print(str(row_count2))