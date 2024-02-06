class Dispositivo:
    def __init__(self, marca:str, modelo:str, cor:str):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ligado = False

    def ligar(self):
        if self.marca == "Negativo":
            return "Explodiu"
        else: 
            if self.ligado == False:
                self.ligado = True
                return f"{self.modelo} está ligando."
            else:
                return f"O aparelho está ligando."
       
    def desligar(self):
        if self.ligado:
            self.ligado = False
            return f"{self.modelo} está desligando."
    
class Smartphone(Dispositivo):
    def __init__(self, marca: str, modelo: str, cor: str, sistema_operacional:str):
        super().__init__(marca, modelo, cor,)
        self.sistema_operacional = sistema_operacional
        
    def fazer_chamada(self, numero:str):
        if self.ligado:
            return f"O smartphone {self.modelo} está fazendo uma chamada para o {numero}"
        else:
            return "Ligue o smartphone"
    
class Notebook(Dispositivo):
    def __init__(self, marca: str, modelo: str, cor: str, ssd: bool):
        super().__init__(marca, modelo, cor)
        self.sdd = ssd

    def acessar_site(self,site:str):
        if self.ligado:
            return f"O notebook {self.modelo} está acessando o site {site}"
        else:
            return "Ligue o notebook"

smart1 = Smartphone(marca="Samsung", modelo="S23", cor="Prata", sistema_operacional="Android")
smart2 = Smartphone(marca="Apple", modelo="Iphone 14", cor="Branco", sistema_operacional="IOS")

note1 = Notebook(marca="Dell", modelo="G15", cor="Preto", ssd=True)

tablet1 = Dispositivo(marca="Negativo", modelo="Do Governo", cor="Preto")
tablet2 = Dispositivo(marca="Samsung", modelo="X", cor="Preto")


print(smart1.ligar())
print(smart1.fazer_chamada("8599999999"))
print(smart1.desligar())
print(smart1.fazer_chamada("8599999999"))

print(smart2.ligar())
print(smart2.fazer_chamada("8599999999"))
print(smart2.desligar())
print(smart2.fazer_chamada("8599999999"))

print(note1.ligar())
print(note1.acessar_site("www.google.com"))
print(note1.desligar())

print(tablet1.ligar())
print(tablet2.ligar())

