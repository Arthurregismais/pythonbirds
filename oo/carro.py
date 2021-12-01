"""
Você deve criar uma classe carro que vai possuir dois atributos
compostos por outras duas classes:

1) motor
2) direção

O motor terá a responsabilidade de controlar a velocidade. ele
oferece os seguintes atributos:

1) Atributo de dado velocidade

2) Método Acelerar, que deverá aumentar a velocidade em uma
unidade

3) Método Frear, que deverá decrementar a velocidade em duas
unidades

A direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos:

1) Valor de direção com valores possíveis:  Norte, Sul, Leste, Oeste
2) Método girar pra direita, e método girar pra esquerda

N - cima

S - baixo

L - direita

O - esquerda

  N
O   L
  S

    Exemplo:
    #testando motor:
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> motor.frear()
    >>> motor.velocidade
    0


    #testando direção:

    >>> direção = Direção()
    >>> direção.direção_atual
    'Norte'
    >>> direção.virar_a_direita()
    >>> direção.direção_atual
    'Leste'
    >>> direção.virar_a_direita()
    >>> direção.direção_atual
    'Sul'
    >>> direção.virar_a_direita()
    >>> direção.direção_atual
    'Oeste'
    >>> direção.virar_a_direita()
    >>> direção.direção_atual
    'Norte'
    >>> direção.virar_a_esquerda()
    >>> direção.direção_atual
    'Oeste'
    >>> direção.virar_a_esquerda()
    >>> direção.direção_atual
    'Sul'
    >>> direção.virar_a_esquerda()
    >>> direção.direção_atual
    'Leste'
    >>> direção.virar_a_esquerda()
    >>> direção.direção_atual
    'Norte'

    #Testando classe Carro:

    >>> carro = Carro()
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direção()
    'Norte'
    >>> carro.virar_a_esquerda()
    >>> carro.calcular_direção()
    'Oeste'
    >>> carro.virar_a_direita()
    >>> carro.calcular_direção()
    'Norte'
    >>> carro.virar_a_direita()
    >>> carro.calcular_direção()
    'Leste'
"""


class Motor:
    velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0


class Direção:
    direção_atual = 'Norte'

    rotação_a_direita_dct = {
        'Norte': 'Leste', 'Leste': 'Sul', 'Sul': 'Oeste', 'Oeste': 'Norte'}

    rotação_a_esquerda_dct = {
        'Norte': 'Oeste', 'Oeste': 'Sul', 'Sul': 'Leste', 'Leste': 'Norte'}

    def virar_a_direita(self):
        self.direção_atual = self.rotação_a_direita_dct[self.direção_atual]

    def virar_a_esquerda(self):
        self.direção_atual = self.rotação_a_esquerda_dct[self.direção_atual]


class Carro(Motor, Direção):

    def calcular_velocidade(self):
        return self.velocidade

    def calcular_direção(self):
        return self.direção_atual


