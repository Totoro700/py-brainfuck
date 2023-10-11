C=True
B=range
def J(n):
	B=False
	if n<=1:return B
	if n<=3:return C
	if n%2==0 or n%3==0:return B
	A=5
	while A*A<=n:
		if n%A==0 or n%(A+2)==0:return B
		A+=6
	return C
def G(number):
	A=number;D=1,A;E=A-1
	for C in B(2,int(A**.5)+1):
		if A%C==0:
			F=A//C;G=abs(C-F)
			if G<E:E=G;D=C,F
	return D
H='[-]'
def E(ascii):
	I='[-<';C='+'
	if J(ascii):
		E,F=G(ascii-1);K=1;A='>'
		for D in B(E):A+=C
		A+=I
		for D in B(F):A+=C
		A+='>]<'
		for D in B(K):A+=C
		A+=f".{H}";return A
	else:
		E,F=G(ascii);A='>'
		for D in B(E):A+=C
		A+=I
		for D in B(F):A+=C
		A+=f">]<.{H}";return A
while C:
	F=input(': ');A=[]
	for I in list(F):A.append(ord(I))
	D=''
	for ascii in A:D+=E(ascii)
	print(D)