#replace synonyms in text
from nltk.corpus import wordnet as wn
from nltk.corpus import verbnet as vn
from nltk.corpus.reader import wordnet as wn1
from nltk.corpus import brown
import nltk
import re
from cPickle import load
from nltk.stem import PorterStemmer
from itertools import chain
import math
import string
import sys

global wn
global wn1
global get_wn_pos2
global get_wn_pos
global file_name_abs

def get_wn_pos(tag):
	if (not tag):
		return ''
	elif tag.startswith('J'):
		return wn.ADJ
	elif tag.startswith('V'):
		return wn.VERB
	elif tag.startswith('N'):
		return wn.NOUN
	elif tag.startswith('R'):
		return wn.ADV
	else:
		return ''
		
def get_wn_pos2(tag):
	if (not tag):
		return ''
	elif tag.startswith('J'):
		return 'a'
	elif tag.startswith('V'):
		return 'v'
	elif tag.startswith('N'):
		return 'n'
	elif tag.startswith('R'):
		return 'r'
	else:
		return ''


num = int(raw_input("Enter sample number 1-13: "))

if not (1<= num <=13):
	num=1

	
try:
   #open file stream
  file_name="sample" + str(num) + "_summary.txt"
  file = open(file_name, "r")
except IOError:
  print "There was an error opening ", file_name
  sys.exit()


file_text = file.read()

sentences = re.split(r' *[\.\?!][\'"\)\]]* *', file_text)

file.close()

words = []
fword = []
fwords = []
swords = []

stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also','although','always','am','among', 'amongst', 'amoungst', 'amount',  'an', 'and', 'another', 'any','anyhow','anyone','anything','anyway', 'anywhere', 'are', 'around', 'as',  'at', 'back','be','became', 'because','become','becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom','but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven','else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'en_sentcept', 'few', 'fifteen', 'fify', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'i', 'I', 'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'nen_sentt', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own','part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'she', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'thickv', 'thin', 'third', 'this', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves', 'the']

for sentence in sentences:
	if sentence != '' and sentence != ' ':
		swords.append(sentence.split())


ct=0
for sword in swords:
	for word in sword:
		#removing punctuation from words
		if not word.isalpha():
			wordset=list(word)
			word=''
			for i in wordset:
				if i.isalpha() or i=='-':
					word+=i
		
		#removing stopwords
		if word.lower() not in stopwords and word!='':
			fword.append(word)
			
	if fword:
		fwords.append(fword)
	else:
		sentences.remove(sentences[len(fwords)+ct])
		ct+=1
	
	fword = []

def wordrank(tagged_context, word, pos):
	nodes = []
	if pos!=wn.VERB and not word.istitle() and len(word)>=2:
		synonyms = wn.synsets(word, pos)
	else:
		synonyms = []
	
	for pair in tagged_context:
		if pair[0].istitle() or len(pair[0])<=2:
				break
		try:
			ss = wn.synsets(pair[0], get_wn_pos(pair[1]))
		except wn1.WordNetError:
			ss = None
		if ss:
			nodes += ss
	
	context_len = len(nodes)
	syn_len = len(synonyms)
	nodes = nodes + synonyms
	n_nodes = len(nodes)
	
	w = [[0 for i in range(n_nodes)] for j in range(n_nodes)]
	i=0
	while i<n_nodes:
		j=i+1
		while j<n_nodes:
			if wn.path_similarity(nodes[i], nodes[j]):
				w[i][j]=w[j][i]=wn.path_similarity(nodes[i], nodes[j])
			else:
				w[i][j]=w[j][i] = 0
			j+=1
		i+=1
	
	ws = [0 for i in range(n_nodes)]
	wsprev = [0 for i in range(n_nodes)]
	s=0
	f=0
	d=0.85
	def checkall(ws, wsprev):
		for i in range(n_nodes):
			if math.fabs(ws[i]-wsprev[i])>0.00001:
				return False
		
		return True

	while True:
		for i in range(n_nodes):
			f=0
			for j in range(n_nodes):
				s=0
				if w[j][i]!=0:
					for k in range(n_nodes):
						s+=w[j][k]
					#print 'denom=',s
					s=w[j][i]/s
					#print 's=', s
					s*=wsprev[j]
					#print 'final s=', s
					
				f+=s	
				#print 'f=', f
			
			wsprev[i]=ws[i]
			ws[i]=(1-d)+d*f
		#print ws, wsprev
		if checkall(ws, wsprev):
			break
		wsprev=list(ws)
		
	#print ws
	
	syn_ws = ws[context_len:]
	best_syn = None
	if syn_ws:
		best_syn_ws = max(syn_ws)
		best_syn = synonyms[syn_ws.index(best_syn_ws)]
	
	if	best_syn:
		return best_syn
	else:
		return None
	
input = open('t2.pkl', 'rb')
tagger = load(input)
input.close()

synonyms_dict = dict()

def best(word, syn):
	best_syn=word
	if len(best_syn)<=5:
		return best_syn
	#print syn.lemma_names
	for l in syn.lemma_names:
		if len(l)<len(best_syn):
			best_syn=l
	#print best_syn
	return best_syn

def plural(word):
	
	if word.endswith("s"):
		if not (word.endswith("ss") or word.endswith("ings") or word.endswith("us") or word.endswith("os")):
			return True
		else:
			return False
	else:
		return False
		
#def verb_form(word, syn):

	#if word.endswith("ing"):
	#	if syn.endswith("e"):
	#		syn=syn.rstrip("e")+"ing"
	#	else:
	#		syn=syn+"ing"
	
	#if word.endswith("ed"):
	#	if syn.endswith("e"):
	#		syn=syn+"d"
	#	elif syn.endswith("y"):
	#		syn=syn.rstrip("y")+"ied"
	#	elif syn.endswith("ed"):
	#	else:		
	#		syn=syn+"ed"
	
	#if word.endswith("s"):
	#	syn=syn+"s"
		
	#return syn
i=0
synonyms_dict = dict()
for tokens in fwords:
	tagged = tagger.tag(tokens)
	for pair in tagged:
		pos=get_wn_pos(pair[1])
		best_syn=wordrank(tagged, pair[0], pos)
		word=pair[0]
		if best_syn:
			best_syn_str=best(word, best_syn)
			if pos==wn.NOUN and plural(word):
				if best_syn_str.endswith("y"):
					best_syn_str = best_syn_str.rstrip("y") + "ies"
				elif not best_syn_str.endswith('s'):
					best_syn_str+='s'
			elif pos==wn.VERB:
				best_syn_str = verb_form(word, best_syn_str)
			#print best_syn_str
			#print best_syn_str
			if word!=best_syn_str:
				synonyms_dict[word]=best_syn_str

for sword in swords:
	for word in sword:
		end=''
		for char in string.punctuation:
			if word.endswith(char):
				end = word[-1]
				word = word[:len(word)-1]
				#print word
				break
		if word in synonyms_dict.keys():
			sword[sword.index(word+end)]="<"+synonyms_dict[word]+end+">"
			
			#print synonyms_dict[word]
			
try:
  # open file stream
  file_name_abs=file_name.rstrip(".txt")+ "_abstract.txt"
  file = open(file_name_abs, "w")
except IOError:
  print "There was an error opening ", file_name
  sys.exit()
  
for sword in swords:
	if sword:
		for word in sword:
			if word == sword[-1]:
				file.write(word)
			else:
				file.write(word + " ")
		file.write(".\n")
file.close()
			
