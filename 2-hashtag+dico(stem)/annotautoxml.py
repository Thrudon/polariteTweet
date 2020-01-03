import unidecode
import re
import json
from pandas.io.json import json_normalize
from nltk.stem.snowball import FrenchStemmer

'''todo'''
#comment
datatoxml = '../tweetsTrain.json'
outputxml = 'dataTrain.xml'

#Stemming fonction
#take message and stem words to build array
def stem(msg, stopwords):
	stemmer = FrenchStemmer()
	lem = []
	words = re.split("[ |,|.|;|!|?|\"|\'|-]", msg)
	for word in words:
		if word:
			if (word[0]!="#" and word not in stopwords):
				lem.append(stemmer.stem(word))
			elif (word[0]=="#"):
				lem.append(word)
	return lem

#Formated string in XML
xmltofile = "<root>"

#Load stopwords
stopwords = []
fileStopWord=open("stopwordstem.txt","r")
for line in fileStopWord :
	if line.find('\n') > 0:
		line = line[0:line.find('\n')]
		stopwords.append(line)
fileStopWord.close()

#Load pos dico
pos = []
filePosWord=open("positif.txt","r")
for line in filePosWord :
	if line.find('\n') > 0:
		line = line[0:line.find('\n')-1]
		pos.append(line)
pos.extend(['#jevotemacron','#macronpresident','#votezmacron','#ensemble'])
filePosWord.close()

#load neg dico
neg = []
fileNegWord=open("negatif.txt","r")
for line in fileNegWord :
	if line.find('\n') > 0:
		line = line[0:line.find('\n')-1]
		neg.append(line)
neg.extend(['#jevoteelledegage','#handicap','#honte','#franceinsoumise','#nonaufn','#sansmoile7mai','#lepennon','#soumis','#boulet','#rendeznousmelenchon','#toutsaufmacron','#jamaismacron','#disqualifiee','#jamaispresidente','#sorcellerie','#fhaine'])
fileNegWord.close()

#Load msg
with open(datatoxml) as json_data:
	jTweet = json_normalize(json.load(json_data))


#print(jTweet["tweet"][0][0]["message"])
countneg = 0
countpos = 0
msg = ""
annot = ""
xmlstr = ""
end = len(jTweet["tweet"][0])
#end = 3

#Translate tweet in stemmed msg and annot to XML
for i in range(end):
	countpos = 0
	countneg = 0
	msgarray = []
	msg = jTweet["tweet"][0][i]["message"]
	msg = unidecode.unidecode(msg)
	msg = msg.lower()
	msg = msg.replace("&", " ")
	msg = msg.replace("<", " ")
	msg = msg.replace(">", " ")
	msgarray = stem(msg, stopwords)
	#print(msg)
	for t in msgarray:
		if t in pos:
			countpos += 1
		elif t in neg:
			countneg += 1
	#print(countpos)
	#print(countneg)
	if (countpos>1 and countneg>3): 
		annot = "mixte"
	elif (countneg>1): 
		annot = "negatif"
	elif (countpos>1): 
		annot = "positif"
	else :
		annot = "neutre"
	#if (annot!="neutre"):
	xmlstr = "<tweet>\n<message>"+msg+"</message>\n<type>"+annot+"</type>\n</tweet>\n"
	xmltofile = xmltofile+xmlstr

#End formated XML
xmltofile = xmltofile+"</root>"

#Write XML
with open(outputxml, 'w') as outfile:
    outfile.write(xmltofile)
