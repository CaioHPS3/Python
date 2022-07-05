class Continente:
	
#Construtor que inicialize o
#nome do continente
	def __init__(self, nome='SemNome'):
		self.nome=nome
		self.paises=[]

#Um método que permita adicionar países aos continentes
	def Pais(self, n, p, d):
		novo_pais={'nome':n, 'populacao':p, 'dimensao':d}

		self.paises.append(novo_pais)

#Um método que retorne a dimensão total do continente
	def dTotal(self):
		somaTotal=0.0
		for cont in self.paises:
			somaTotal+=cont['dimensao']

		return somaTotal
		# print(somaTotal)

#Um método que retorne a população total do continente
	def pTotal(self):
		somaTotal=0.0
		for cont in self.paises:
			somaTotal+=cont['populacao']

		return somaTotal
		# print(somaTotal)
#Um método que retorne a população do continente
#Um método que retorne o país com maior população no continente
	def paisMaiorP(self):
		aux=self.paises.copy()
		aux.sort(key=lambda x: x['populacao'])
		return aux[-1]

#Um método que retorne o país com menor população no continente
	def paisMenorP(self):
		aux=self.paises.copy()
		aux.sort(key=lambda x: x['populacao'])
		return aux[0]

#Um método que retorne o país de maior dimensão territorial no continente
	def paisMaiorD(self):
		aux=self.paises.copy()
		aux.sort(key=lambda x: x['dimensao'])
		return aux[-1]

#Um método que retorne o país de menor dimensão territorial no continente
	def paisMenorD(self):
		aux=self.paises.copy()
		aux.sort(key=lambda x: x['dimensao'])
		return aux[0]

#Um método que retorne a razão territorial do maior pais em relação ao menor país.
	def razaoDimenMaiorMenor(self):
		maiorDimen=self.paisMaiorD()
		menorDimen=self.paisMenorD()
		return maiorDimen['dimensao']/menorDimen['dimensao']