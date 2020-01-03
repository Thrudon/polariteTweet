# coding: utf8
##Functions
#Seek word in vectors
def seekword(word, vectors, sumvect):
	for i in len(vectors):
		if (word == vectors[0]):
			for i in len(sumvect):
				sumvect[i] += vectors[i+1]

##Construct Vector representation file
##Load vectors
vectors = []
with open("word2vec.txt") as vec:
	line = vec.readline()
	line = vec.readline()
	while line:
		wordline = line.split()
		vectors.append(wordline)
print("loaded")

##File Train
f = io.open("Train.csv", "w", encoding="UTF-8")
tree = ElementTree.parse("dataTrain.xml")
root=tree.getroot()

for msg in root.findall("./tweet"):
	polariteElem = tweet.find("./type")
	polarite = polariteElem.text
	#msg_str=ElementTree.tostring(msg,encoding="unicode")
	msgElem = tweet.find("./message")
	msg_str = msgElem.text
	msgvect = [0] * 100
	for mot in re.split("[\s,:\".'?!@]",msg_str):
		if(re.search("//.",mot)==None and re.search("co/.",mot)==None and mot!="http" and mot!=":" and mot!=";" and mot!="," and mot!="." and mot!="" and mot!="@"): #élimine les liens,':',',','.'
			seekword(mot, vectors, msgvect)
	for i in len(msgvect):
		f.write(msgvect+",")
	f.write(polarite+"\n")
f.close

##File Test
f = io.open("Test.csv", "w", encoding="UTF-8")
tree = ElementTree.parse("dataTest.xml")
root=tree.getroot()

for msg in root.findall("./tweet"):
	polariteElem = tweet.find("./type")
	polarite = polariteElem.text
	#msg_str=ElementTree.tostring(msg,encoding="unicode")
	msgElem = tweet.find("./message")
	msg_str = msgElem.text
	msgvect = [0] * 100
	for mot in re.split("[\s,:\".'?!@]",msg_str):
		if(re.search("//.",mot)==None and re.search("co/.",mot)==None and mot!="http" and mot!=":" and mot!=";" and mot!="," and mot!="." and mot!="" and mot!="@"): #élimine les liens,':',',','.'
			seekword(mot, vectors, msgvect)
	for i in len(msgvect):
		f.write(msgvect+",")
	f.write(polarite+"\n")
f.close
