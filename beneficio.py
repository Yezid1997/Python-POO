from cuenta import Cuenta

class Beneficio(Cuenta):
    def __init__(self, nombre, apellido, cedula, edad, dineroAhorrado):
        super().__init__(nombre, apellido, cedula, edad, dineroAhorrado)
    
    def validarUsuario(self):
        return self.getEdad() >= 18 and self.getEdad() < 28 
    
    def mostrar(self):
        self.bonificacion = self.dineroAhorrado * 0.05
        return f'Cliente: {self.getNombre()} {self.getApellido()} \nCédula: {self.getCedula()} \nEdad: {self.getEdad()} \nCantidad de la cuenta -> Total: ${self.getDineroAhorrado()} + Bonificación(5%): ${self.bonificacion} = ${self.getDineroAhorrado() + self.bonificacion}'

beneficio1 = Beneficio("Juan", "Revelo", "123", 22, 50000)
print(beneficio1.mostrar())