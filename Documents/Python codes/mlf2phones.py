# Detecta los fonemas del archivo mlf
# Crea el dummy dictionay
entrada = open("words.mlf", 'r')
salida = open("monophones0", "w")
dicti = open("dictionary", "w")

lines=entrada.readlines()
entrada.close()
fonemas=[]

for i in range(len(lines)):
	if (("MLF" not in lines[i]) and ("." not in lines[i])):
		pal=""
		for q in lines[i]:
			if (q not in "1234567890 ") and (q not in "\n") and (q not in "\r") and (q not in "\t"):
				pal+=q
		fonemas.append(pal)		

fonemas=list(set(fonemas))
for i in range(len(fonemas)):
	salida.write(fonemas[i]+"\n")
	dicti.write(fonemas[i]+"\t"+fonemas[i]+"\n")

dicti.close()
salida.close()
	

