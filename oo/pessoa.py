class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=19):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome} {id(arthur)}'


if __name__ == '__main__':
    arthur = Pessoa(nome='Arthur')
    adevar = Pessoa(arthur, nome='Adevar')
    print(Pessoa.cumprimentar(arthur))
    print(id(arthur))
    print(arthur.cumprimentar())
    print(arthur.nome)
    print(arthur.idade)
    print(adevar.filhos)
    for filho in adevar.filhos:
        print(filho.nome)
    adevar.sobrenome = 'Mais'
    del adevar.filhos
    arthur.olhos = 1
    del arthur.olhos
    print(adevar.__dict__)
    print(arthur.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(adevar.olhos)
    print(arthur.olhos)
    print(id(Pessoa.olhos)), print(id(arthur.olhos)), print(id(adevar.olhos))
