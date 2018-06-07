from tez import *

for line in open('text.txt', 'r'):
	h_sense, yandex, ash = line.split(';')
	for h_word in h_sense.split(','):
		for y_word in [translate(x) for x in yandex.split(',')]:
			res = compare(h_word, y_word)
			if res > 0.66:
				# совпало
			else:
				try: 
					# не совпало?

