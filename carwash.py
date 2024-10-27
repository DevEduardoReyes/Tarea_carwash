
class cliente:
    def __int__(self, identidad, nombre, apellido):
        self.identidad = identidad
        self.nombre = nombre
        self.apellido = apellido

class auto:
    def __int__(self,tipo,year,asientos):
        self.tipo = tipo
        self.year = year
        self.asientos = asientos

class orden(cliente,auto):
    def __init__(self,identidad, nombre, apellido,tipo, year, asientos,fecha_inicio, fecha_fin):
        auto.__int__(self,tipo, year, asientos)
        cliente.__int__(self, identidad, nombre, apellido)
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

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

    def Expotador(self):
        if self.year <= 2000:
            precio = 1500
        elif self.year >2000 and self.year < 2010:
            precio =2000
        else:
            precio = 3500
        return precio

nuevo = orden(1999,"eduardo",'reyes','camioneta',2018,2,18,20)

print(nuevo.lavado_aspirado())
