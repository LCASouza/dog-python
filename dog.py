class Dog:
    
    def __init__(self, nome):
        self.nome = nome
        self.brincando = False
        self.mordendo = False
        self.dormindo = False


    def verificarAcaoAtual(self, acao):
        if self.brincando == True and acao != 'brincar' and acao != '!brincar':
            self.brincando = False
            print(f'{self.nome} nao esta mais brincando!')

        if self.mordendo == True and acao != 'morder' and acao != '!morder':
            self.mordendo = False
            print (f'{self.nome} parou de morder!')

        if self.dormindo == True and acao != 'dormir' and acao != '!dormir':
            self.dormindo = False
            print (f'{self.nome} acordou!')


    def nomeDog(self, nome):
        self.nome = nome


    def brincar(self):
        if not self.brincando:
            print(f'O {self.nome} agora esta brincando!')
            self.brincando = True
            return

        if self.brincando:
            print(f'O {self.nome} ja esta brincando!')
    
    def stopBrincar(self):
        if not self.brincando:
            print(f'O {self.nome} nao esta brincando!')
            return

        if self.brincando:
            self.brincando = False
            print(f'O {self.nome} parou de brincar!')

    def morder(self):
        if not self.mordendo:
            print(f'O {self.nome} agora esta mordendo!')
            self.mordendo = True
            return

        if self.mordendo:
            print(f'O {self.nome} ja esta mordendo!')

    def stopMorder(self):
        if not self.mordendo:
            print(f'O {self.nome} nao esta mordendo!')
            return

        if self.mordendo:
            self.mordendo = False
            print(f'O {self.nome} parou de morder!')

    def dormir(self):
        if not self.dormindo:
            print(f'O {self.nome} agora esta dormindo!')
            self.dormindo = True
            return

        if self.dormindo:
            print(f'O {self.nome} ja esta dormindo!')

    def stopDormir(self):
        if not self.dormindo:
            print(f'O {self.nome} ja esta acordado!')
            return

        if self.dormindo:
            print(f'O {self.nome} acabou de acordar!')
            self.dormindo = False