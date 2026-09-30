def hipotenusa():

	while True:

		try:
			print('\n [C] Cateto\n [H] Hipotenusa')
			pergunta = str(input('Deseja calcular um dos CATETO ou HIPOTENUSA: ').strip().upper())

			 #Cateto
			if pergunta == 'H':
				cateto_1 = float(input('Qual o tamanho do 1° cateto: ').strip().replace(",", "."))
				cateto_2 = float(input('Qual o tamanho do 2° cateto: ').strip().replace(",", "."))
				calculo = str((cateto_1 ** 2 + cateto_2 ** 2) ** (1/2))
				pergunta = 'hipotenusa'

			#Famosa Hipotenusa!
			elif pergunta == 'C': 
				hipotenusa = float(input('Qual o tamanho da hipotenusa: ').strip().replace(",", "."))
				cateto_2 = float(input('Qual o tamanho do 2° cateto: ').strip().replace(",", "."))
				calculo = str((hipotenusa ** 2 - cateto_2 ** 2) ** (1/2))
				pergunta = '1° cateto'

			else:
				print ('-  Ops! Valor inválido, tente novamente.')
				continue


		#tratamento de input errado
		except: 
			print ('-  Ops! Valor inválido, tente novamente.')
			continue

		#tratando resultados inválido de em float
		if 'j' in calculo:
			print('---\nCalculo inválido, tente novamente com novos valores!!\n---')
			continue

		#devolvendo o //str para //float
		calculo = float(calculo)
		return calculo, pergunta

