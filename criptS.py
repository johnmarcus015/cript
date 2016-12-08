m=input("Digite a mensagem: ")
k=input("Digite a chave: ").upper()
v=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
vK1=[]
cK=len(k)

def alinharCaracteres(k, v, vK1):
	x,p0=0,0
	for i in range(0, len(v)):
		if k == v[i]:p0=i
	for i in range(p0, len(v)):
		vK1.append(v[i])
	for i in range(0, p0):
		vK1.append(v[i])
	return vK1

def mudarMensagem(m, k, v, vK1):
	for i in range(0, len(m)):
		if k == m[i].upper():
			print (i)
			vK1 = alinharCaracteres(k,v,vK1)
			print (v)
			print (vK1)
	for i in range(0, len(v)):
		if k == v[i]:
			print ("%c = %c" %(v[i], vK1[i]))

#vK1 = alinharCaracteres(k,v, vK1)
#print (vK1)
mudarMensagem(m,k,v,vK1)



