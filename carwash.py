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

