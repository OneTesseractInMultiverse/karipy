# una lista al igual que un conjunto, es una coleccion de elementos solo que las listas
# si conservan la nocion de orden y si podemos tener elementos repetidos. Ademas las listas,
# Son ciudadanos de primera clase en Python. 

# una lista la podemos simplemente declarar con parentesis cuadrados.
lista_vacia = []

# una lista la podemos declarar tambien como un literal
lista_de_nombres = ['nombre', 'nombre2', 'nombre3']
lista_de_numeros = [1, 2, 4, 6, 2, 1, 4, 5, 6, 1, 3, 4]
lista_malota  = [23, 'nombre1', 3.1426, set([2, 3, 4]), ['otra', 34, 'x']]

# Para acceder los elementos de una lista, utilizamos indices. Los indices son valores,
# numericos que referencia la posicion relativa de un elemento dentro de una lista.
# Es muy importante tomar en cuenta que las posiciones de los elentos de una lista se
# cuentan a partir de la posicion 0 ya que lo que determinan es la cantidad de 
# desplazamientos en memoria, por lo que el primero elemento se cuentra cuando tenemos
# un desplazamiento de 0.

def exists_in_list(value, list):
	return value in list

# Para acceder al primer elemento de una lista entonces necesitamos:
print("El primer elemento de la lista es: {elemento}".format(elemento=lista_de_nombres[0]))

print('It is {veracity} that name exists in lista_de_nombres'.format(veracity=exists_in_list('nombre', lista_malota)))

print(lista_malota[4][0])

# Para agregar elementos a una lista de manera dinamica, utilizamos el metodo 'lista.append(valor_por_agregar)'

lista_de_nombres.append('nombre_agregado')
print(lista_de_nombres)

print('--------------------------------')

matrix = []

for row in range(0, 5):
	values = []
	for column in range(0, 5):
		values.append("{},{}".format(row, column))
		
	matrix.append(values)  # cada vez que llegamos a esta linea, agregamos la lista que conforma una nueva fila en la matrix


# Aca recorremos cada una de las filas y columnas de la matrix y vamos concatenando los 
# elementos que conforman una fila en una sola cadena de caracteres y luego imprimimos 
# cada una de las filas. 
for row in matrix:
	row_str = ''
	for column in row:
		row_str = row_str + '[{value}]'.format(value=column)
	print(row_str)
	
print(matrix[2][3])


# TAREA!
'''
Modificar el codigo anterior para que imprima una matriz en la que si el numero de columna es par entonces ponga un 0 
y si el numero de columa es impar entonces ponga un 1:

[0][1][0][1][0]
[0][1][0][1][0]
[0][1][0][1][0]
[0][1][0][1][0]
[0][1][0][1][0]

Modificar el codigo anterior para que genere la siguiente matriz:

[1][0][0][0][0]
[0][1][0][0][0]
[0][0][1][0][0]
[0][0][0][1][0]
[0][0][0][0][1]

'''
	
		
		







