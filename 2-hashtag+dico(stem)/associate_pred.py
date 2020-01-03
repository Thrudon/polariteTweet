def numbers_to_strings(argument): 
    switcher = {
		0: "autre",
		1: "positif",
        2: "negatif",
		3: "mixte",
    } 
  
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(argument, "nothing") 


out = open(r"res.txt", "w")
f = open(r"exemple.txt","r")
f2 = open(r"out.txt","r")

linesf=f.readlines()
linesf2=f2.readlines()

for i in range(0,len(linesf)):
	linef=linesf[i]
	linef2=linesf2[i]
	id=linef.split(" ",1)[0]
	polarite=numbers_to_strings(int(linef2))	
	out.write(id+" "+polarite+"\n")
