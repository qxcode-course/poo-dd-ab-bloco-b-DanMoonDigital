class Chinela:
    def __init__(self):
        self.tamanho = 0

    def getTamanho(self):
        return self.tamanho
    
    def setTamanho(self, valor: int):
        if valor < 20 or valor > 50:
            print("Erro: tamanho deve estar entre 20 e 50")
        elif valor % 2 != 0:
            print("Erro: o tamanho deve ser um número par.")
        else:
            self.tamanho = valor
        print("Tamanho válido registrado!")

chinela = Chinela()

while chinela.getTamanho() == 0:
    print("Digite seu tamanho de chinela:")
    tamanho = int(input())
    chinela.setTamanho(tamanho)
print("Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())