from tez import *
from json import dump

def compare(S1, S2):
	ngrams = [S1[i:i+3] for i in range(len(S1))]
	# print(ngrams)
	count = 0
	for ngram in ngrams:
		count += S2.count(ngram)

	return count/max(len(S1), len(S2))

def measure(A, B):
	def translate_list(A):
		for i in range(len(A)):
			A[i] = translate(A[i])
		return A

	def _in(a, B):
		for b in B:
			if compare(a, b) > 0.6:
				print(a,b)
				return True
		return False

	def countcat(A, B):
		rex = 0
		toremove = []
		for a in A:
			if _in(a, B):
				rex += 1
				toremove += [a]
		for a in toremove:
			A.remove(a)
		return rex

	def countsubcat(A, B):
		rex = 0
		toremove = []
		for a in A:
			try:
				if _in(tez[a], B):
					rex += 0.5
					toremove += [a]
			except KeyError:
				pass
		for a in toremove:
			A.remove(a)
		return rex

	def countsubsubcat(A, B):
		rex = 0
		for a in A:
			for b in B:
				try:
					if compare(tez[b], tez[a]) > 0.6:
						rex += 0.25
				except KeyError:
					pass
		return rex

	A = translate_list(A)
	B = translate_list(B)

	r1, r2, r3, r4 = countcat(A, B), countsubcat(A, B), countsubcat(B, A), countsubsubcat(A, B)
	rez = sum([r1, r2, r3, r4])
	deb = "(%s, %s, %s, %s)" % (r1, r2, r3, r4)
	try:
		rez /= max(len(A), len(B))
	except ZeroDivisionError:
		rez = 0
	return rez, deb

# i = 1
# for CT, YT, HA, AT in [ _.split('^') for _ in open().readlines() if _ ]:
# 	CT = CT.split(',')
# 	YT = YT.split(',')
# 	HA = HA.split(',')
# 	AT = AT.split(',')
# 	y = measure(CT, YT)
# 	n = measure(CT, HA)
# 	a = measure(CT, AT)
# 	rez.update({i:{'YT':y,'HA':n,'AT':a}})

# print(rez)

if __name__ == '__main__':
	# print(measure())
	# print(measure(["солнце", "облако",   "рисунок",   "абажур",   "солнцезащитный крем", "собака"], 
	# 	          ["звезда", "растение", "искусство", "материал", "косметика",           "одежда"]))
	# print(measure(["солнце", "обалко",   "искусство", "абажур",   "солнцезащитный крем", "собака"], 
	# 	          ["звезда", "растение", "рисунок",   "материал", "косметика",           "одежда"]))
	# print(measure(["солнце", "облако",   "рисунко",   "материал", "солнцезащитный крем", "собака"], 
	# 	          ["звезда", "растение", "искусство", "косметика","одежда"]))

	rez = {}
	i = 1
	print([ _.split('^') for _ in open("auto_tag_text.txt").readlines() if _ ])
	for CT, YT, HA, AT in [ _.split('^') for _ in open("auto_tag_text.txt").readlines() if _ ]:
		CT = [x.strip() for x in CT.split(',')]
		YT = [x.strip() for x in YT.split(',')]
		HA = [x.strip() for x in HA.split(',')]
		AT = [x.strip() for x in AT.split(',')]
		y, yd = measure(CT[:], YT)
		n, nd = measure(CT[:], HA)
		a, ad = measure(CT[:], AT)
		rez.update({
			i :{'CT':CT, 
			'YT' :{'yd':yd, 'score': y, 'tags': YT},
			'HA' :{'nd':nd, 'score': n, 'tags': HA},
			'AT' :{'ad':ad, 'score': a, 'tags': AT}}
		})
		i+=1

	yt = 0
	ha = 0
	at = 0
	for i in rez.keys():
		yt += rez[i]['YT']['score']
		ha += rez[i]['HA']['score']
		at += rez[i]['AT']['score']

	rez.update({'yt':yt})
	rez.update({'ha':ha})
	rez.update({'at':at})
	dump(rez, open('rez.json', 'w'), ensure_ascii=0, indent=4)
	print(yt, ha, at)
