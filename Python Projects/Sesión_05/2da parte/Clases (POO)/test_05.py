"""
    Programación Orientada a Objetos
    Participación

Requerimientos:
    - Crear una Clase Alumno
    - Debe tener un atributo de nacionalidad con el valor "Peruano"
    - Tendrá 3 notas, la nota inicial de c/u será de 0
    - Crear un método que indicará el promedio del alumno
    - Crear un método que indicará si el alumno está aprobado
    o no de acuerdo a su promedio
    - Las notas serán pasadas por parámetro al momento de instanciar la clase
    - Crear un método para obtener el nombre y distrito de residencia del alumno
    - Instanciar la clase para el caso de 2 alumnos necesariamente
"""


class Alumno:
    def __init__(self, alumno, distrito):
        self.alumno = alumno
        self.distrito = distrito
        self.nacionalidad = "Peruana"
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.estado = False

    def notas(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def promedio(self):
        return (self.n1 + self.n2 + self.n3) / 3

    def aprobado_desaprobado(self):
        if self.promedio() > 10:
            return "aprobado"
        else:
            return "desaprobado"

    def informacion(self):
        return self.distrito


alum_1 = Alumno("Max", "El Tambo")
alum_1.notas(10, 14, 15)
alum_2 = Alumno("Elisse", "Chilca")
alum_2.notas(10, 0, 20)

for alum in [alum_1, alum_2]:
    print(f"Las notas ingresadas son : {alum.n1}, {alum.n2}, {alum.n3}")
    print(
        f"El alumno {alum.alumno} tiene la nacionalidad de {alum.nacionalidad} y es del distrito de {alum.informacion()}.")
    print(f"El promedio del alumno {alum.alumno} es : {alum.promedio():.02f} y está {alum.aprobado_desaprobado()}.\n")