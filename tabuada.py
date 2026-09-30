def tabuada():

	while True:
		
		print(f' Multiplicação {'[X]':>5}\n Divisão{'[/]':>12}\n Subtração{'[-]':>10}\n Adição{'[+]':>13}')
		função = str(input(f'Vai ser uma tabuada de: ').strip().upper()) 
		match função:
			
			case 'X':
				print ('-'*17,'Multiplicaçao selecionado','-'*17)
				X()
				break
			case '/':
				print ('-'*17,'Divisão selecionada','-'*17)
				Div()
				break
			case '-':
				print ('-'*17,'Subtração selecionado','-'*17)
				Sub()
				break
			case '+':
				print ('-'*17,'Adição selecionada','-'*17)
				Adi()
				break
			case _:
				print('Numero inválido tente novamente')
				continue



def X(): 			#multiplicação
	while True:	
		try:
			base = int(input('Escolha um número: ').strip())
			final = int(input('Tabuada de 1 ao: ').strip())
			print('#' * 17)
		except:
			print('Numero inválido tente novamente')
			continue
		for final in range(1,final+1):
			alinha = int(len(str(base))) + 1
			calculo = base * final
			print(f"| {base} X {final:>2} = {calculo:>{alinha}} |")
		break



def Div():			 #divisão
        while True:     
                try:
                        base = int(input('Escolha um número: ').strip())
                        final = int(input('Tabuada de 1 ao: ').strip())
                        print('#' * 17)
                except:
                        print ('Numero inválido tente novamente')
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
                        print('#' * 17)
                except:
                        print('Numero inválido tente novamente')
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
                        print('#' * 17)
                except:
                        print('Numero inválido tente novamente')
                        continue
                for final in range(1,final+1):
                        alinha = int(len(str(base))) + 1
                        calculo = base + final
                        print(f"| {base} + {final:>2} = {calculo:>{alinha}} |")
                break



while True: # Iniciar programa
	print ('#'*17)
	iniciar = input('[1] Tabuada\n[2] Hipotenusa \n[0] Para sair\n ----:   ')


	if iniciar == '1':
		tabuada()


	elif iniciar == '2':   #Hipotenusa
		from triangulo import hipotenusa #Chama a função 
		valor, lado = hipotenusa()
		print('#'*17,f'\n|{lado}: tem o valor de {valor:.2f}|\n')

	else:
		break #acabou!
