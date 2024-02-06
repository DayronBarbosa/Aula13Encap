class Animal:
    def __init__(self, nome:str, raca:str, idade:int, cor:str, peso:float) -> None:
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.cor = cor
        self.peso = peso
    
    def comer(self,comida:str):
        return f"O animal {self.nome} está comendo a comida {comida}"
    
    def dormir(self):
        return f"O animal {self.nome} está dormindo"
    
    def ver_informacoes(self):
        return f"""
        Nome: {self.nome}
        Raça: {self.raca}
        Idade: {self.idade}
        Cor: {self.cor}
        Peso: {self.peso}
    """
    
class Cachorro(Animal):
    def __init__(self, nome: str, raca: str, idade: int, cor: str, peso: float) -> None:
        super().__init__(nome, raca, idade, cor, peso)
    
    def pegar_bolinha(self):
        return f"O cachorro {self.nome} foi pegar a bolinha"


class Gato(Animal):
    def __init__(self, nome: str, raca: str, idade: int, cor: str, peso: float, cor_do_olho:str) -> None:
        super().__init__(nome, raca, idade, cor, peso)
        self.cor_do_olho = cor_do_olho
    
    def amassar_paozinho(self):
        return f"O gato {self.nome} está amassando pãozinho"
    

gatinho = Gato(nome="Salem", raca="Pé duro", idade=10, cor="Preto", peso=2.3, cor_do_olho="Amarelo")
cachorrinho = Cachorro(nome="Spike", raca="Vira lata", idade=3, cor="Caramelo", peso=5.8)
porquim = Animal(nome="Nhoc", raca="Baconzito", idade=1, cor="Rosinha", peso=20)


print(gatinho.comer(comida="Peito de Frango"))
print(gatinho.dormir())
print(gatinho.amassar_paozinho())


print(cachorrinho.comer(comida="Costelinha"))
print(cachorrinho.dormir())
print(cachorrinho.pegar_bolinha())



print(porquim.comer(comida="Pé de galinha"))
print(porquim.dormir())