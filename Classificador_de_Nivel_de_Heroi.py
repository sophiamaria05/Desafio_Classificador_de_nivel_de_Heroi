nome  = input("Insira os dados do heroi\nNome: ")
xp = None
while (xp == None):
	xp = input("Quantidade de xp: ")
	try:
		xp = int(xp)
	except:
		xp = None
		print("Entrada de xp inválida!\nFavor inserir a quantidade de xp em numeros inteiros...\n")

if (xp<=1000):
	print("O Herói de nome >>", nome,"<<está no nível de >> Ferro <<")

elif (xp<=2000):
	print("O Herói de nome >>", nome,"<<está no nível de >> Bronze <<")

elif (xp<=5000):
	print("O Herói de nome >>", nome,"<<está no nível de >> Prata <<")

elif (xp<=7000):
	print("O Herói de nome >>", nome,"<<está no nível de >> Ouro<<")

elif (xp<=8000):
	print("O Herói de nome >>", nome,"<<está no nível de >> Platina <<")

elif (xp<=9000):
	print("O Herói de nome >>", nome,"<<está no nível de >> Ascendente <<")

elif (xp<=10000):
	print("O Herói de nome >>", nome,"<<está no nível de >> Ferro <<")

else :
	print("O Herói de nome >>", nome,"<<está no nível de >> Radiante <<")

