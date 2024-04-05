# evaluaciones.py

from pizza import Pizza

# a. Mostrar los valores de los atributos de clase sin crear una instancia
print("Ingredientes proteicos disponibles:", Pizza.ingredientes_proteicos)
print("Ingredientes vegetales disponibles:", Pizza.ingredientes_vegetales)
print("Tipos de masa disponibles:", Pizza.tipos_de_masa)

# b. Verificar si 'salsa de tomate' está en la lista dada usando el método estático
elemento_a_buscar = "salsa de tomate"
lista_de_comprobacion = ["salsa de tomate", "salsa bbq"]
esta_presente = Pizza.validar_elemento(elemento_a_buscar, lista_de_comprobacion)
print(f"¿Está '{elemento_a_buscar}' en {lista_de_comprobacion}? {esta_presente}")

# c. Crear una instancia y solicitar al usuario que realice un pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d. Mostrar los ingredientes y tipo de masa seleccionados, y si la pizza es válida
print("\nDetalle del pedido realizado:")
print(f"Ingrediente proteico: {mi_pizza.ingrediente_proteico}")
print(f"Primer ingrediente vegetal: {mi_pizza.primer_ingrediente_vegetal}")
print(f"Segundo ingrediente vegetal: {mi_pizza.segundo_ingrediente_vegetal}")
print(f"Tipo de masa: {mi_pizza.tipo_de_masa}")
print(f"¿Es una pizza válida? {'Sí' if mi_pizza.es_valida else 'No'}")

# e. Intentar mostrar si Pizza es una pizza válida sin crear una instancia (debería dar error)
# Esto debería fallar ya que es_valida es un atributo de instancia, no de clase.
try:
    print(f"¿Es Pizza una pizza válida? {Pizza.es_valida}")
except AttributeError as error:
    print(f"Error detectado: {error}")