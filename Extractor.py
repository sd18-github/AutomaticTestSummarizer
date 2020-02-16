import sys
import re
import math
from nltk.stem import PorterStemmer

from fifth import rat

global n_sent
global file_name
global math
global file_name2
global file_name1
global file_name_exr

try:
    # open file stream
    if len(file_name1) > 1:
        file_name = str(file_name1)
    else:
        file_name = "sample1.txt"
    file = open(file_name, "r")
except IOError:
    print("There was an error opening ", file_name)
    sys.exit()

file_text = file.read()
file.close()

# split the text into sentences based on periods, exclamation marks, brackets, quotation marks, etc
sentences = re.split(r' *[.?!][\'")\]]* *', file_text)

# Take ratio as input from the user
ratio = int(rat)
# int(raw_input("Enter ratio (30-100):"))
if not (30 <= ratio <= 100):
    ratio = 33

words = []
fword = []
fwords = []
swords = []
stemmer = PorterStemmer()
stopwords = ['a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone',
             'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an',
             'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at',
             'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand',
             'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom', 'but',
             'by', 'call', 'can', 'cannot', 'cant', 'co', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail',
             'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else', 'elsewhere',
             'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'en_sentcept',
             'few', 'fifteen', 'fify', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty',
             'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have',
             'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him',
             'himself', 'his', 'how', 'however', 'hundred', 'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is',
             'it', 'its', 'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may',
             'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must',
             'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'nen_sentt', 'nine', 'no', 'nobody',
             'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one',
             'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own',
             'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 'same', 'see', 'seem', 'seemed', 'seeming',
             'seems', 'serious', 'several', 'she', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so',
             'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system',
             'take', 'ten', 'than', 'that', 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there',
             'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'thickv', 'thin', 'third',
             'this', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too',
             'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'us', 'very',
             'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where',
             'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while',
             'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would',
             'yet', 'you', 'your', 'yours', 'yourself', 'yourselves', 'the']

for sentence in sentences:
    if sentence != '' and sentence != ' ':
        swords.append(sentence.split())

ct = 0
for sword in swords:
    for word in sword:
        # removing punctuation from words
        if not word.isalpha():
            wordset = list(word)
            word = ''
            for i in wordset:
                if i.isalpha() or i == '-':
                    word += i

        # removing stopwords and stemming
        if word.lower() not in stopwords and word != '':
            fword.append(stemmer.stem(word))

    if fword:
        fwords.append(fword)
    else:
        sentences.remove(sentences[len(fwords) + ct])
        ct += 1

    fword = []

# no. of sentences in the document
n_sent = len(fwords)
# adjacency matrix for graph
w = [[0 for i in range(n_sent)] for j in range(n_sent)]

# Loop to calculate similarity of sentences based on number of common (stemmed) words
i = 0
while i < len(fwords):
    j = i + 1
    while j < len(fwords):
        count = 0
        for word in fwords[i]:
            if word in fwords[j]:
                count += 1
        if len(fwords[i]) != 1 and len(fwords[j]) != 1:
            w[i][j] = w[j][i] = (count / (math.log(len(fwords[i]) + math.log(len(fwords[j])))))
        j += 1
    i += 1

d = 0.85
ws = [0 for i in range(n_sent)]
wsprev = [0 for i in range(n_sent)]
s = 0
f = 0


def checkall(ws, wsprev):
    # to check whether scores have converged
    for i in range(n_sent):
        if math.fabs(ws[i] - wsprev[i]) > 0.00001:
            return False
    return True


# loop to calculate weighted scores of each node (sentence) iteratively, using the edge scores
while True:
    for i in range(n_sent):
        f = 0
        for j in range(n_sent):
            s = 0
            if w[j][i] != 0:
                for k in range(n_sent):
                    s += w[j][k]
                s = w[j][i] / s
                s *= wsprev[j]
            f += s
        wsprev[i] = ws[i]
        ws[i] = (1 - d) + d * f

    if checkall(ws, wsprev):
        break  # break if scores have converged
    wsprev = list(ws)

sentrank = []
for i in range(n_sent):
    sentrank.append((i, ws[i]))


def get_key1(item):
    return item[1]


def get_key0(item):
    return item[0]


# sorting the weights in descending order
sentrank = sorted(sentrank, key=get_key1, reverse=True)

# calculating length of summary based on ratio
sumlength = int(math.ceil(float((n_sent * ratio) / 100)))

# re-sorting sentences with highest weights in the original order
fsentrank = sorted(sentrank[:sumlength], key=get_key0)

file_name_exr = file_name.rstrip(".txt") + "_summary.txt"
try:
    # open file stream
    file = open(file_name_exr, "w+")
except IOError:
    print("There was an error writing to", file_name)
    sys.exit()

# writing sentences to file
file.write(sentences[0] + '.\n')  # first sentence is always included
for i in fsentrank:
    if get_key0(i) != 0:
        file.write(sentences[get_key0(i)].strip() + '.\n')

file.close()
