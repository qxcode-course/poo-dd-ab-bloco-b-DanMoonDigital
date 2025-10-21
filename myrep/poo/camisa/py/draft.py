class Camisa:
    def __init__(self):
        self.tamanho = 0

    def getTamanho(self):
        return self.tamanho
    
    def setTamanho(self, valor: int):
        tamanho_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor in tamanho_validos:
            self.tamanho = valor
        else:
            print("Valor inválido, tente PP, P, M, G, GG ou XG")

camisa = Camisa()

while camisa.getTamanho() == 0:
    print("Digite seu tamanho de Roupa:")
    tamanho = input ()
    camisa.setTamanho(tamanho)

print("Parabéns, você comprou uma roupa tamanho", set)