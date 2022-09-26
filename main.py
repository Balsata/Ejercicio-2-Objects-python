class Alumno:

    def inicio (self, nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def resultado (self):
        if self.nota < 5:
            print( "El alumno esta reprobado")
        else:
            print("El alumno ha aprobado")

alumno = Alumno()
alumno.inicio("Jose",3)


print(alumno.resultado())

