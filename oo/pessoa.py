class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=19):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):

    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3
    pass


if __name__ == '__main__':
    arthur = Mutante(nome='Arthur')
    adevar = Homem(arthur, nome='Adevar')
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
    print(Pessoa.olhos)
    print(adevar.olhos)
    print(arthur.olhos)
    print(id(Pessoa.olhos)), print(id(arthur.olhos)), print(id(adevar.olhos))
    print(Pessoa.metodo_estatico()), print(arthur.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe()), print(arthur.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonima')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(arthur, Pessoa))
    print(isinstance(arthur, Homem))
    print(arthur.olhos)
    print(arthur.cumprimentar())
    print(adevar.cumprimentar())

