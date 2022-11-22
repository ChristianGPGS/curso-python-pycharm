class Taza_cafe():
    def __init__(self, temperatura, tipo_cafe):
        self.temperatura = temperatura
        self.tipo_cafe = tipo_cafe

    def __str__(self):
        print(self.temperatura, self.tipo_cafe)
