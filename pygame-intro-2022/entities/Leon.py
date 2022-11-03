import random

class Leon():

    def __init__(self,nombre = "Sin nombre"):
        self.nombre = nombre
        self.vida = 100  #Almacenamos la vida del animal, 100 por defecto
        self.fuerza = random.randint(1,5) #5 el más fuerte
        self.edad = 0 #Cuanto más viejo, menos fuerza
        self.resistencia = random.uniform(1.0,2.0)

    def atacar(self):
        multiplicador = random.randint(1,3)
        golpe = self.fuerza * multiplicador
        if multiplicador == 3:
            print("Golpe crítico !!!")
        return golpe

    def comer(self):
        energia = random.randint(1,3)
        if self.vida + energia > 100:
            self.vida = 100
        else:
            self.vida = self.vida + energia

    def morir(self):
        print("El león",self.nombre,"ha muerto.")
        raise SystemExit()

    #True si lo ha esquivado; False si recibe el golpe
    def esquivar(self):
        if random.randint(1,10) == 5:
            return True
        else:
            return False

    def recibir_golpe(self, golpe):
        if not self.esquivar():
            self.vida = self.vida - int (golpe / self.resistencia)
            if self.vida <= 0:
                self.morir()
        else:
            print("El leon "+self.nombre+" ha esquivado el golpe")

    def __str__(self):
        return ("{}. {} {}".format(self.nombre,self.fuerza,self.vida))
