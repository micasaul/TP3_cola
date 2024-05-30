# # Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,casa de comic a la que pertenece 
# # (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:
# # a. eliminar el nodo que contiene la información de Linterna Verde;
# # b. mostrar el año de aparición de Wolverine;
# # c. cambiar la casa de Dr. Strange a Marvel;
# # d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
# # e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
# # f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# # g. mostrar toda la información de Flash y Star-Lord;
# # h. listar los superhéroes que comienzan con la letra B, M y S;
# # i. determinar cuántos superhéroes hay de cada casa de comic.
from Lista_enlazada import search, remove, show_list

super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "DC Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hank Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos."
  }
]
lista_superh=[]

for superheroe in super_heroes:
  lista_superh.append(superheroe)    

# a. eliminar el nodo que contiene la información de Linterna Verde;
def elim_lint_verde (lista):
  lint= remove(lista, 'nombre', 'Linterna Verde')
  if lint is not None:
    print("Linterna Verde fue eliminado")

# b. mostrar el año de aparición de Wolverine;
def año_wolverine (lista):
  pos=search(lista, 'nombre', 'Wolverine')
  if pos is not None:
    print(f"El año de aparicion de Wolverine es {lista[pos]['año_aparicion']}")
  else:
    print("Wolverine no aparece")
  
# c. cambiar la casa de Dr. Strange a Marvel;
def casa_strange (lista):
  pos=search(lista, 'nombre', 'Doctor Strange')
  if pos is not None:
    lista[pos]['casa_comic'] = "Marvel Comics"
    print(lista[pos])
  else:
    print("Dr Strange no aparece")

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
def traje_armadura (lista):
  for superheroe in lista:
    if "traje" in superheroe['biografia'] or "armadura" in superheroe['biografia']:
      print(f"{superheroe['nombre']} usa un traje o armadura")

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
def antes_63 (lista):
  for superheroe in lista:
    if superheroe['año_aparicion'] <= 1963:
      print(f"{superheroe['nombre']} de {superheroe['casa_comic']} aparecio en {superheroe['año_aparicion']}")
   
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
def cap_maravilla (lista):
  for superheroe in lista:
    if superheroe['nombre'] == "Capitana Marvel" or superheroe['nombre'] == "Mujer Maravilla":
      print(f"{superheroe['nombre']} pertenece a {superheroe['casa_comic']}")
  
# g. mostrar toda la información de Flash y Star-Lord;
def flash_star (lista):
  for superheroe in lista:
    if superheroe['nombre'] == "Flash" or superheroe['nombre'] == "Star-Lord":
      print(superheroe)

# h. listar los superhéroes que comienzan con la letra B, M y S;
def b_m_s (lista):
  letras=["B", "M", "S"]
  bms=[]
  for superheroe in lista:
    if superheroe['nombre'][0] in letras:
      bms.append(superheroe)
  return bms

# i. determinar cuántos superhéroes hay de cada casa de comic.
def super_casa (lista):
  marvel = 0 
  dc = 0
  for superheroe in lista:
    if superheroe['casa_comic'] == "Marvel Comics":
      marvel +=1
    if superheroe['casa_comic'] == "DC Comics":
      dc +=1
  print(f"hay {marvel} superheroes que pertenecen a marvel, y {dc} superheroes que pertenecen a dc")

elim_lint_verde(lista_superh)
print()
año_wolverine(lista_superh)
print()
casa_strange(lista_superh)
print()
traje_armadura(lista_superh)
print()
antes_63(lista_superh)
print()
cap_maravilla(lista_superh)
print()
flash_star(lista_superh)
print()
bms= b_m_s(lista_superh)
show_list('Lista de superheroes cuyo nombre empieza con b, m o s:', bms)
print()
super_casa(lista_superh)