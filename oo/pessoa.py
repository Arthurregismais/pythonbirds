class Pessoa:
    def __init__(self, nome=None, idade=19):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {self.nome} {id(p)}'


if __name__ == '__main__':
    p = Pessoa('Arthur')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Henrique'
    print(p.nome)
    print(p.idade)
