class Veiculo:
    def __init__(self, marca:str, modelo:str, cor:str, ano:int):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ano = ano

        self.__velocidade_atual = 0

    def getMarca(self):
        return self.self__marca
    
    def setMarca(self, nova_marca):
        self.__marca = nova_marca
        return "Marca alterada."
    
    def getModelo(self):
        return self.self__modelo
    
    def setModelo(self, novo_modelo):
        self.__modelo = novo_modelo
        return "Modelo alterado."
    
    def getCor(self):
        return self.self__cor
    
    def setCor(self, nova_cor):
        self.__cor = nova_cor
        return "Cor alterada."
    
    def getAno(self):
        return self.self__ano
    
    def setMarca(self, novo_ano):
        self.__ano = novo_ano
        return "Marca alterada."
    
    def acelerar(self,velocidade_acelerada):
        self.__velocidade_atual = self.__velocidade_atual + velocidade_acelerada
        return f"O veículo {self.getModelo()} está a {self.__velocidade_atual} acelerando..."
    
    def freiar(self):
        self.__velocidade_atual = self.__velocidade_atual - 10
        return f"O veículo {self.getModelo()} está freiando."

    def buzinar(self):
        return "Som indefinido"
    
    
    