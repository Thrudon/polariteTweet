# coding: utf8
from xml.etree import ElementTree
import re
import io
from random import randint

f = io.open("index_extract.txt", "w", encoding="UTF-8")
mots=[]

##Construction de l'index
##Fichier Train
tree = ElementTree.parse("dataTrain.xml")
root=tree.getroot()

for msg in root.findall("./tweet/message"):
	msg_str = msg.text
	for mot in re.split("[\s,:\".'?!@]",msg_str):
		if(mot not in mots):
			if(re.search("//.",mot)==None and re.search("co/.",mot)==None and mot!="http" and mot!=":" and mot!=";" and mot!="," and mot!="." and mot!="" and mot!="@"): #élimine les liens,':',',','.'
				mots.append(mot)
				f.write(unicode("<"+mot+">"+"<"+str(mots.index(mot)+1)+"> \n"))

##Fichier Test
tree = ElementTree.parse("dataTest.xml")
root=tree.getroot()

for msg in root.findall("./tweet/message"):
	msg_str = msg.text
	for mot in re.split("[\s,:\".'?!@]",msg_str):
		if(mot not in mots):
			if(re.search("//.",mot)==None and re.search("co/.",mot)==None and mot!="http" and mot!=":" and mot!=";" and mot!="," and mot!="." and mot!="" and mot!="@"): #élimine les liens,':',',','.'
				mots.append(mot)
				f.write(unicode("<"+mot+">"+"<"+str(mots.index(mot)+1)+"> \n"))

f.close()


##Creer la representation SVM
##Fichier Train
f = io.open("svm_Train.svm", "w")			
tree = ElementTree.parse("dataTrain.xml")
root=tree.getroot()

for tweet in root.findall("./tweet"):
	msgElem = tweet.find("./message")
	msg_str = msgElem.text
	polariteElem = tweet.find("./type")
	polarite = polariteElem.text
	if ("neutre"==polarite):
		f.write(unicode("0 "))
	elif ("positif" == polarite):
		f.write(unicode("1 "))
	elif ("negatif"==polarite):
		f.write(unicode("2 "))
	elif ("mixte"==polarite):
		f.write(unicode("3 "))
	tweet=msg_str.split(" ")
	for mot in mots:
		if (mot in tweet):
			f.write(unicode(str(mots.index(mot)+1)+":"))
			compteur=0
			for mot2 in tweet: 
				if(mot==mot2): 
					compteur=compteur+1
					
			f.write(unicode(str(compteur)+" "))	
	f.write(unicode("\n"))		
f.close()		

##Fichier Test
f = io.open("svm_Test.svm", "w")			
tree = ElementTree.parse("dataTest.xml")
root=tree.getroot()

for tweet in root.findall("./tweet"):
	msgElem = tweet.find("./message")
	msg_str = msgElem.text
	polariteElem = tweet.find("./type")
	polarite = polariteElem.text
	if ("neutre"==polarite):
		f.write(unicode("0 "))
	elif ("positif"==polarite):
		f.write(unicode("1 "))
	elif ("negatif"==polarite):
		f.write(unicode("2 "))
	elif ("mixte"==polarite):
		f.write(unicode("3 "))
	tweet=msg_str.split(" ")
	for mot in mots:
		if (mot in tweet):
			f.write(unicode(str(mots.index(mot)+1)+":"))
			compteur=0
			for mot2 in tweet: 
				if(mot==mot2): 
					compteur=compteur+1
					
			f.write(unicode(str(compteur)+" "))	
	f.write(unicode("\n"))		
f.close()		
