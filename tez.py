import requests

tez = {
	"солнце" :"звезда",
	"гусеница" :"насекомое",
	"облако" :"небо",
	"цветок" :"растение",
	"дом" :"строение",
	"рисунок" :"искусство",
	"бумага" :"материал",
	"карандашный рисунок" :"рисунок",
	"абажур" :"мебель",
	"пакет" :"емкость",
	"конверт" :"почта",
	"солнцезащитный крем" :"косметика",
	"футболка" :"одежда",
	"собака" :"животное",
	"хвост" :"конечность",
	"щенок" :"миленький",
	"язык" :"орган чувств",
	"уши" :"слух",
}

dic = {
	"drawing": "рисунок",
	"cartoon": "мультфильм",
}

class FuzzyDict(dict):
	def __init__(self, items = None, cutoff = .6):
		"""Construct a new FuzzyDict instance
		items is an dictionary to copy items from (optional)
		cutoff is the match ratio below which mathes should not be considered
		cutoff needs to be a float between 0 and 1 (where zero is no match
		and 1 is a perfect match)"""
		super(FuzzyDict, self).__init__()

		if items:
			self.update(items)
		self.cutoff =  cutoff

		# short wrapper around some super (dict) methods
		self._dict_contains = lambda key: \
			super(FuzzyDict,self).__contains__(key)

		self._dict_getitem = lambda key: \
			super(FuzzyDict,self).__getitem__(key)

	def compare(self, S1, S2):
		ngrams = [S1[i:i+3] for i in range(len(S1))]
		# print(ngrams)
		count = 0
		for ngram in ngrams:
			count += S2.count(ngram)

		return count/max(len(S1), len(S2))

	def search(self, lookfor):
		for i in self:
			if self.compare(lookfor, i) > 0.6:
				return i

		return None

	def __contains__(self, lookfor, stop_on_first = False):
		"""Overides Dictionary __contains__ to use fuzzy matching"""
		if self.search(lookfor):
			return True
		else:
			return False

	def __getitem__(self, lookfor):
		matched = self.search(lookfor)

		if not matched:
			raise KeyError(str(lookfor))

		return matched

def translate(word):
	try:
		res = dic[word]
	except KeyError:
		params = {
			"key": "trnsl.1.1.20180607T153100Z.4eaf3b366a2b9327.e9c3cea46c53de5f22b6df313f46cb237e03618b",
			"text": word,
			"lang": "en-ru"
		}
		resp = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate", params=params)
		# print(j_resp)
		translated = resp.json().get("text", None)
		if translated:
			length = len(translated[0].split(" "))
			if length > 1:
				# TODO
				pass
			else:
				res = translated[0]

	return res

# try:
# 	x = tez["рисунки"]
# except Exception as e:
# 	# print(x)
# 	pass

# for key in tez.keys():
# 	if len(key.split(" ")) > 1:
# 		for key_words
# 	if compare(key, "рисунки") > 0.6:
# 		x = tez[key]

# print(x)

# t = translate("car")
# print(t)
d = FuzzyDict(items=tez)
print(d.search("солнцезащитный"))

