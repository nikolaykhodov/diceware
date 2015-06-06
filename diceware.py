# -*- encoding: utf-8 -*-

import os
import sys

def load_words(f):
	words = []
	for line in open(f):
		parts = line.strip().split('\t', 1)

		# skip lines which don't match the format: (number) (word)
		if len(parts) < 2:
			continue

		words.append(parts[1].strip())
	return words

def get_random_word(words):
	N = 16
	scaleFactor = reduce(lambda x, y: 256 * x + ord(y), list(os.urandom(N)), 0) * 1.0 / (256 ** N)

	return words[int(scaleFactor * len(words))]

def main():
	# how many words should be a passphrase
	amountOfWords = int(sys.argv[1])

	# custom word list
	if len(sys.argv) >= 3:
		filename = sys.argv[2]
	else:
		filename = 'diceware.wordlist.asc'
	words = load_words(filename)

	# generate
	passphrase = ''
	for i in range(amountOfWords):
		passphrase += get_random_word(words) + ' '

	# output
	print passphrase

if __name__ == '__main__':
	main()
