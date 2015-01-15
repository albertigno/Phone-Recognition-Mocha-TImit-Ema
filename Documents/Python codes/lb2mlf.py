# Crea el mlf a partir del .lb
tipo="fsew0_"
#numero de archivos a tomar
nfiles=460

salida = open("words.mlf", "w")
salida.write("#!MLF!#\n")

for i in range(nfiles):
	n=str(i+1)
	q=n.rjust(3,'0')
	nombre=tipo+q+".lb"
	archivo=open(nombre, 'r')
	lines=archivo.readlines()
	archivo.close()
	#Escribir el encabezado
	encab="\""+"*/"+q+".lab"+"\""+"\n"
	salida.write(encab)
	#Escribir linea por linea
	for k in range(len(lines)):
		salida.write(lines[k])
	salida.write("\n.\n")
	
	



