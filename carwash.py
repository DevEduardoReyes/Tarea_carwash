from abc import ABC, abstractmethod


class cliente(ABC):
    def __int__(self, identidad, nombre, apellido):
        self.identidad = identidad
        self.nombre = nombre
        self.apellido = apellido


    @abstractmethod
    def lavado_aspirado(self):
        pass
    @abstractmethod
    def Shamposeado(self):
        pass
    @abstractmethod
    def Exportador(self):
        pass

class auto(ABC):
    def __int__(self,tipo,year,asientos):
        self.tipo = tipo
        self.year = year
        self.asientos = asientos



class Orden(cliente,auto):
    def __init__(self,identidad, nombre, apellido,tipo, year, asientos,fecha_inicio, fecha_fin):
        auto.__int__(self,tipo, year, asientos)
        cliente.__int__(self, identidad, nombre, apellido)
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def arreglo(self):
        return {
            "identidad": self.identidad,
            "Nombre del cliente": self.nombre,
            "Apellido": self.apellido,
            "Tipo de auto": self.tipo,
            "Anio del auto": self.year,
            "asientos": self.asientos,
            "fecha de inicio": self.fecha_inicio,
            "fecha final": self.fecha_fin
        }
    @staticmethod
    def mostrar(dic):
        for i in dic:
            print(i,":",dic[i])


    def lavado_aspirado(self):
        if self.tipo == 'turismo' or self.tipo == "coche":
            precio = 200
        else:
            precio =500
        return precio

    def Shamposeado(self):
        if self.asientos <= 2:
            precio = 3000
        else :
            precio = 5000
        return precio

    def Exportador(self):
        if self.year <= 2000:
            precio = 1500
        elif self.year >2000 and self.year < 2010:
            precio =2000
        else:
            precio = 3500
        return precio

orden1 = Orden(8011999,"eduardo",'reyes','camioneta',1999,4,18,20)

orden1.mostrar(orden1.arreglo())
print("Costo del trabajo:",orden1.Exportador())
print()
orden2= Orden(3141975,"Marixa",'Benites','turismo',2011,2,1,5)
orden2.mostrar(orden2.arreglo())
print("Costo del trabajo:",orden2.Shamposeado())
print()

orden3 =Orden(201810235,"Jose",'Benites','camion',2022,6,15,30)
orden3.mostrar(orden3.arreglo())
print("Costo del trabajo:",orden3.lavado_aspirado())
print()

