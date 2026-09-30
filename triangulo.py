def hipotenusa():

	while True:


		print('\n [C] Cateto\n [H] Hipotenusa')
		pergunta = str(input('Deseja calcular um dos CATETO ou HIPOTENUSA: ').strip().upper())

		if pergunta == 'C':
			cateto_1 = float(input('Qual o tamanho do 1° cateto: ').strip())
			cateto_2 = float(input(f'Qual o tamanho do 2° cateto: ').strip())
			calculo = (cateto_1 ** 2 + cateto_2 ** 2) ** (1/2)
			pergunta = '1° cateto'

		elif pergunta == 'H':	
			hipotenusa = float(input(f'Qual o tamanho da hipotenusa: ').strip())
			cateto_2 = float(input(f'Qual o tamanho do 2° cateto: ').strip())
			calculo = (hipotenusa ** 2 - cateto_2 ** 2) ** (1/2)
			pergunta = 'hipotenusa'


		else:
			print ('-  Ops! Valor inválido, tente novamente.')
			continue

		
		return calculo, pergunta

