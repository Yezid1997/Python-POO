from usuario import Usuario

class Cuenta(Usuario):
    def __init__(self, nombre, apellido, cedula, edad, dineroAhorrado):
        super().__init__(nombre, apellido, cedula, edad)
        self.dineroAhorrado = dineroAhorrado

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido = apellido

    def getCedula(self):
        return self.cedula

    def setCedula(self, cedula):
        self.cedula = cedula
    
    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getDineroAhorrado(self):
        return self.dineroAhorrado

    def mostrar(self):
        return f'Cliente: {self.getNombre()} {self.getApellido()} Cédula: {self.getCedula()} Edad: {self.getEdad()} Dinero disponible: {self.getDineroAhorrado()} '

    def ingresar(self, cantidad):
        if (cantidad > 0):
            self.dineroAhorrado += cantidad
    
    def retirar(self, cantidad):
        if (cantidad > 0):
            self.dineroAhorrado -= cantidad

