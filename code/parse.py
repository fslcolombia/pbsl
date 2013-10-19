personas = []
with open('../AUTHORS', 'r') as autores:
    for line in autores.readlines():
        #FIXME: Reemplazar esto por un regex cuando los aprendamos
        # en especifico, verificar que la linea tenga las comas y tenga un correo al final.
        if '@' not in line:
            continue
        # Partimos la linea en las comas y limpiamos cualquier espacio extra
        columnas = [x.strip() for x in line.split(',')]
        personas.append(columnas)

# persona es una lista de listas
# en cada persona, la primera componente es el nombre de usuario de github
# la segunda es el nombre de pila y la tercera es el correo.
for persona in personas:
    username, name, email = persona
    print name