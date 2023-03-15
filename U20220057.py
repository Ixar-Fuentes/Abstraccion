class Viaje():
    
    def __init__(self,lugar):
        self.lugar=lugar
        self.horaSalida=8
        self.horaRegreso=5

    
    def nombreLugar (self):
        print(f"Luagar de el viaje:{self.lugar}")

    
    def Ida(self):
        print(f"Hora de salida: {self.horaSalida}")

    def Regreso(self):
        print(f"Hora de Regreso: {self.horaRegreso}")
        
class Playa(Viaje):
    def __init__(self,lugar):
        super().__init__(lugar)
        self.horaSalida=7
        self.horaRegreso=6

    def nombreLugar (self):
        print(f"Lugar de el viaje: {self.lugar}")
        


    def Ida(self):
        print(f"Hora de salida: {self.horaSalida}")

    def Regreso(self):
        print(f"Hora de Regreso: {self.horaRegreso}")


class Lago(Viaje):
    def __init__(self,lugar):
        super().__init__(lugar)
        self.horaSalida=9
        self.horaRegreso=4

    def nombreLugar (self):
        print(f"Lugar de el viaje: {self.lugar}")
        


    def Ida(self):
        print(f"Hora de salida: {self.horaSalida}")

    def Regreso(self):
        print(f"Hora de Regreso: {self.horaRegreso}")


class Turicentro(Viaje):
    def __init__(self,lugar):
        super().__init__(lugar)
        self.horaSalida=5
        self.horaRegreso=3

    def nombreLugar (self):
        print(f"Luagar de el viaje: {self.lugar}")
        
    def Ida(self):
        print(f"Hora de salida: {self.horaSalida}")

    def Regreso(self):
        print(f"Hora de Regreso: {self.horaRegreso}")
        
        
salidita1 = Playa("El tunco")
salidita2 = Lago("Ilopango")
salidita3 = Turicentro("Termos de el rio")

salidita1.nombreLugar()
salidita1.Ida()
salidita1.Regreso()
salidita2.nombreLugar()
salidita2.Ida()
salidita2.Regreso()
salidita3.nombreLugar()
salidita3.Ida()
salidita3.Regreso()
        
