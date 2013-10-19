with open('../AUTHORS', 'r') as autores:
    for line in autores.readlines():
        if '@' not in line:
            continue
        columnas = line.split(',')
        nombre = columnas[1].strip()
        print(nombre)