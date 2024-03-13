import random

class EstrategiaAtaque:
    def atacar(self):
        raise NotImplementedError

# Implementaciones concretas de los comportamientos de ataque
class AtaqueCuerpoACuerpo(EstrategiaAtaque):
    def atacar(self):
        return "ataque cuerpo a cuerpo"

class AtaqueADistancia(EstrategiaAtaque):
    def atacar(self):
        return "ataque a distancia"

# movimiento
class EstrategiaMovimiento:
    def moverse(self):
        raise NotImplementedError

#caminar
class Caminar(EstrategiaMovimiento):
    def moverse(self):
        return "Caminando"

class Montar(EstrategiaMovimiento):
    def moverse(self):
     return "Cabalgando"






class UnidadMilitar:
    def __init__(self, nombre, estrategia_ataque, estrategia_movimiento):
        self.nombre = nombre
        self.estrategia_ataque = estrategia_ataque
        self.estrategia_movimiento = estrategia_movimiento

    def atacar(self):
        return self.estrategia_ataque.atacar()

    def moverse(self):
        return self.estrategia_movimiento.moverse()

class Soldado(UnidadMilitar):
    def __init__(self):
        super().__init__("Soldado", AtaqueCuerpoACuerpo(), Caminar())

class Arquero(UnidadMilitar):
    def __init__(self):
        super().__init__("Arquero", AtaqueADistancia(), Caminar())

class Caballero(UnidadMilitar):
    def __init__(self):
        super().__init__("Caballero", AtaqueCuerpoACuerpo(), Montar())

# Clase principal del juego
class JuegoEstrategia:
    def __init__(self):
        self.unidades = []

    def agregar_unidad(self, unidad):
        self.unidades.append(unidad)

    def atacar(self, unidad_atacante, unidad_atacada):
        print(f"{unidad_atacante.nombre} está atacando a {unidad_atacada.nombre}:")
        print(f" - {unidad_atacante.atacar()}")
        print()

    def jugar(self):
        for unidad in self.unidades:
            print(f"{unidad.nombre}:")
            print(f" - {unidad.atacar()}")
            print(f" - {unidad.moverse()}")
            print()


juego = JuegoEstrategia()
juego.agregar_unidad(Soldado())
juego.jugar()


unidad_atacante = Soldado()
unidad_atacada = Arquero()
juego.atacar(unidad_atacante, unidad_atacada)