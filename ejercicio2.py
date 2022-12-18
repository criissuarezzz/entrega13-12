# El malvado gobierno de programación ha prohibido el uso de números. Su tarea, si elige
# aceptarla, es devolver números, sin usar números.
# Problemas:
# • No puede usar literales numéricos en su código fuente.
# • No puede usar la propiedad de longitud directamente en su código.
# Meta:
# • Tienes que devolver 'Puedo escribir números como 1, 2, 3'

from word2number import w2n



def convertir(*args):

    lista =""

    for i in args:

            lista+=str(w2n.word_to_num(i))

    return lista



print("Puedo escribir números como",convertir('one'),",", convertir('two'),",", convertir('three'),".")