# Calculadora Python

#Digitar valor na para operação


def soma():
	x = int(input('Digite o primeiro valor: '))
	y = int(input('Digite o segundo valor: '))
	z = x + y
	print ('A soma é igual a: ' + str(z))

def subtração():
	x = int(input('Digite o primeiro valor: '))
	y = int(input('Digite o segundo valor: ')) 
	z = x - y
	print ('A subtração é igual a: ' + str(z))

def multiplicação():
	x = int(input('Digite o primeiro valor: '))
	y = int(input('Digite o segundo valor: '))
	z = x * y
	print ('A operação é igual a: ' + str(z))

	
def divisão ():
	x = int(input('Digite o primeiro valor: '))
	y = int(input('Digite o segundo valor: '))
	if y == 0 and x > 0 :
		print ('Denominador incorreto: %d. Digite uma valor maior que 0' %(y))
		começo()
	elif y > 0:
		z = x / y
		print ('A operação é igual a: ' + str(z))

def começo():
    valor = int(input('Digite um valor: 1, 2, 3, 4 \n 1: Soma \n 2: Subtração \n 3: Multiplicação \n 4: Divisão \n'))

    if valor == 1:
        soma()
    elif valor == 2:
        subtração()
    elif valor == 3:
        multiplicação()
    elif valor == 4: 
        divisão() 
    elif valor != range(1,5): #valor <> 1 or valor <> 2 or valor <> 3 or valor <> 4:
        print ('Valor digitado incorreto | Digite um valor para operação corretamente')
        começo()
   
começo()

sim_nao = str(input('Deseja sair da Calculadora? S/N'))

def sair_calculadora():
    if sim_nao == 'S' or sim_nao == 's':
        print('Fim da Calculadora')
    elif sim_nao == 'N' or sim_nao =='n':
        começo()
        
sair_calculadora()
