import unidecode
import re
import json
from pandas.io.json import json_normalize
#Fonction de traduction json vers xml avec tri des informations utiles et formatages des strings messages
def funct(part):
	#Dictionnaire des hashtags et mots cles releve lors de l'analyse de donnees
	neg = "(#jevoteelledegage|#handicap|#honte|#franceinsoumise|#nonaufn|#sansmoile7mai|#lepennon|#soumis|#boulet|#rendeznousmelenchon|#toutsaufmacron|#jamaismacron|#disqualifiee|#jamaispresidente|#sorcellerie|#fhaine|mepris|niquer|nique|saoule|ridicule|alzheimer|haine|saigne[nt]|difficile|con[ne]?|ivre|enormite[s]?|horrible|pietre|guignols|negligees|neglige|chier|mascarade|merde|nul|consternant|affligeante|indigne|risible|KO|perlimpinpin|insecurite|pitoyable|folle|raciste|folle|pathetique|humiliee|humiliation|parasite|mort|boulet|vulgaire|singe|honte|honteux|perdre|fuck|malade|insolence|ecu|nulle|farce|hysterie|mensonges|mensonge|immonde|minable|arrogant|insulteur|parasite|intox|irrespect|mediocrite|mediocres|mediocre|hypocrisie|suicide|hitler|baffe|bafe|baffer|attaquer|attaque|attaques|chaos|impertinence|mal|folle|marionette[s]?|fou[t]?[tre]?|desolidarise[r]?|couille|justif[i]?[e]?[r]?|dece[de]?[e]?[s]?|gogol[e]?[ito]?|chaotique[s]?|ment[i]?[r]?|mens[onges]?|md[r]+|!{3,})"
	pos = "(#jevotemacron|#macronpresident|#ensemble|fier|impressionnant|bien|bravo|merci|fierepragmatique|efficace|rassembleuse|protectrice|clair|convaincant)"

	#Parcour en mode arbre
	xmltofile = "<root>"

	#Lecture du fichier source
	with open('../tweets'+part+'.json') as json_data:
		jTweet = json_normalize(json.load(json_data))
	#Initialisation des varibles
	countneg = 0
	countpos = 0
	msg = ""
	key = ""
	annot = ""
	xmlstr = ""
	end = len(jTweet["tweet"][0])
	print(end)
	#Parcour des tweets
	for i in range(end):
		key = jTweet["tweet"][0][i]["url"]
		key = key.split("/")[5]
		msg = jTweet["tweet"][0][i]["message"]
		msg = unidecode.unidecode(msg)
		msg = msg.lower()
		msg = msg.replace("&", "et")
		msg = msg.replace("<", " ")
		msg = msg.replace(">", " ")
		#Annotation de la polarité
		countpos = len(re.findall(pos, msg))
		countneg = len(re.findall(neg, msg))
		if (countpos!=0 and countneg!=0): 
			annot = "mixte"
		elif (countpos!=0): 
			annot = "positif"
		elif (countneg!=0): 
			annot = "negatif"
		else :
			annot = "neutre"
		#Section a ajouter si on veut annuler l'apprentissage des neutres
		#if (annot != "neutre"):
		xmlstr = "<tweet><id>"+key+"</id><message>"+msg+"</message><type>"+annot+"</type></tweet>"
		xmltofile = xmltofile+xmlstr
		xmltofile = xmltofile+"</root>"

		#Ecriture du fichier final
		with open('data'+part+'.xml', 'w') as outfile:
			outfile.write(xmltofile)

#Faire le procede pour train et test
funct('Train')
funct('Test')