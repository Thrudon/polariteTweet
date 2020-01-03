import unidecode
import re
import json
from pandas.io.json import json_normalize

###########	Train / Test	###############
step = 'Test'

neg = "(#jevoteelledegage|#handicap|#honte|#franceinsoumise|#nonaufn|#sansmoile7mai|#lepennon|#soumis|#boulet|#rendeznousmelenchon|#toutsaufmacron|#jamaismacron|#disqualifiee|#jamaispresidente|#sorcellerie|#fhaine|mepris|niquer|nique|saoule|ridicule|alzheimer|haine|saigne[nt]|difficile|con[ne]?|ivre|enormite[s]?|horrible|pietre|guignols|negligees|neglige|chier|mascarade|merde|nul|consternant|affligeante|indigne|risible|KO|perlimpinpin|insecurite|pitoyable|folle|raciste|folle|pathetique|humiliee|humiliation|parasite|mort|boulet|vulgaire|singe|honte|honteux|perdre|fuck|malade|insolence|ecu|nulle|farce|hysterie|mensonges|mensonge|immonde|minable|arrogant|insulteur|parasite|intox|irrespect|mediocrite|mediocres|mediocre|hypocrisie|suicide|hitler|baffe|bafe|baffer|attaquer|attaque|attaques|chaos|impertinence|mal|folle|marionette[s]?|fou[t]?[tre]?|desolidarise[r]?|couille|justif[i]?[e]?[r]?|dece[de]?[e]?[s]?|gogol[e]?[ito]?|chaotique[s]?|ment[i]?[r]?|mens[onges]?|md[r]+|!{3,})"
pos = "(#jevotemacron|#macronpresident|#ensemble|fier[e]?|impressionnant[e]?|bien|bravo|merci|fiere|pragmatique|efficace|rassembleu[r]?[se]?|protect[eur]?[rice]?|convaincant[e])"

xmltofile = "<root>"

with open('../tweets'+step+'.json') as json_data:
	jTweet = json_normalize(json.load(json_data))

#print(jTweet["tweet"][0][0]["message"])
countneg = 0
countpos = 0
msg = ""
key = ""
annot = ""
xmlstr = ""
end = len(jTweet["tweet"][0])
print(end)
for i in range(end):
	msg = jTweet["tweet"][0][i]["message"]
	msg = unidecode.unidecode(msg)
	msg = msg.lower()
	msg = msg.replace("&", "et")
	msg = msg.replace("<", '"')
	msg = msg.replace(">", '"')
	#print(msg)
	countpos = len(re.findall(pos, msg))
	countneg = len(re.findall(neg, msg))
	countneu = len(re.findall('"', msg))
	#print(countpos)
	#print(countneg)
	if (countneu == 2):
		annot = "neutre"
	else:
		if (countpos!=0 and countneg!=0): 
			annot = "mixte"
		elif (countpos!=0): 
			annot = "positif"
		elif (countneg!=0): 
			annot = "negatif"
		else :
			annot = "nan"
	if (annot != "nan"):
		xmlstr = "<tweet><message>"+msg+"</message><type>"+annot+"</type></tweet>"
		xmltofile = xmltofile+xmlstr

xmltofile = xmltofile+"</root>"

with open('data'+step+'.xml', 'w') as outfile:
    outfile.write(xmltofile)
