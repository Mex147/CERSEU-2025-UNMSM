#Reforzamiento
# 13
from doctest import master

cursos = ["Calculo diferencial", "Circuitos eléctricos I",
          "Programación I", "Circuitos electrónicos I",
          "Sistemas eléctricos de potencia I", "Cálculo integral"]
mcursos = cursos

print(cursos)
print(type(cursos))

mcursos.append("Circuitos eléctricos II")
mcursos.append("Programación II")
mcursos.append("Sistemas eléctricos de potencia II")
mcursos.append("Laboratorio de circuitos eléctricos I")

print(mcursos)