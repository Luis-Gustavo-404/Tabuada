def tabuada():

	while True:
		
		print(f' Multiplicação {'[X]':>5}\n Divisão{'[/]':>12}\n Subtração{'[-]':>10}\n Adição{'[+]':>13}')
		função = str(input(f'Vai ser uma tabuada de: ').strip().upper()) 
		if função == 'X':
			print ('-'*17,'Multiplicaçao selecionado','-'*17)
			X()
			break
		elif função == '/':
			print ('-'*17,'Divisão selecionada','-'*17)
			Div()
			break
		elif função == '-':
			print ('-'*17,'Subtração selecionado','-'*17)
			Sub()
			break
		elif função == '+':
			print ('-'*17,'Adição selecionada','-'*17)
			Adi()
			break
		else:
			print('Numero invalido tente novamente')
			continue


def X(): #multiplicação
	while True:	
		try:
			base = int(input('Escolha um número: ').strip())
			final = int(input('Tabuada de 1 ao: ').strip())
		except:
			print('Numero invalido tente novamente')
			continue
		for final in range(1,final+1):
			alinha = int(len(str(base))) + 1
			calculo = base * final
			print(f"| {base} X {final:>2} = {calculo:>{alinha}} |")
		break


def Div(): #divisão
        while True:     
                try:
                        base = int(input('Escolha um número: ').strip())
                        final = int(input('Tabuada de 1 ao: ').strip())
                except:
                        print ('Numero invalido tente novamente')
                        continue
                for final in range(1,final+1):
                        alinha = int(len(str(base))) + 1
                        calculo = base / final
                        print(f"| {base} ÷ {final:>2} = {calculo:>{alinha}.2f} |")
                break


def Sub(): 			#subtração
        while True:     
                try:
                        base = int(input('Escolha um número: ').strip())
                        final = int(input('Tabuada de 1 ao: ').strip())
                except:
                        print('Numero invalido tente novamente')
                        continue
                for final in range(1,final+1):
                        alinha = int(len(str(base))) + 1
                        calculo = base - final
                        print(f"| {base} - {final:>2} = {calculo:>{alinha}} |")
                break


def Adi():                      #adição
        while True:     
                try:
                        base = int(input('Escolha um número: ').strip())
                        final = int(input('Tabuada de 1 ao: ').strip())
                except:
                        print('Numero invalido tente novamente')
                        continue
                for final in range(1,final+1):
                        alinha = int(len(str(base))) + 1
                        calculo = base + final
                        print(f"| {base} + {final:>2} = {calculo:>{alinha}} |")
                break


while True: # Iniciar programa
	print ('#'*17)
	iniciar = input('Qualquer tecla para Iniciar a Tabuada\n Pressione [0] para sair: ')

	if iniciar == '0':
		break
	else:
		tabuada()
		continue
