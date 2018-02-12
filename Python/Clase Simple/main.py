# IMPLEMENTACION DE LA CLASE "Persona" del archivo clasePersona.py
from clasePersona import Persona

Manu = Persona("Manu", "35", "Masculino")
print Manu

Manu.set_nombre("Andres")
Manu.set_edad("34")
Manu.set_genero("Perruno")
print Manu

print Manu.saludar("Hola a todos!")