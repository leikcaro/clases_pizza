from ingredientes import ingredientes_proteicos, ingredientes_vegetales, tipos_de_masa

class Pizza:
    '''Atributos de clase con los valores posibles para cada tipo de ingrediente'''
    ingredientes_proteicos = ingredientes_proteicos
    ingredientes_vegetales = ingredientes_vegetales
    tipos_de_masa = tipos_de_masa

    def __init__(self):
        self.ingrediente_proteico = None
        self.primer_ingrediente_vegetal = None
        self.segundo_ingrediente_vegetal = None
        self.tipo_de_masa = None
        self.es_valida = False

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    def realizar_pedido(self):
        '''Método para crear una pizza considerando sis ingredientes'''        
        print("Por favor, elija sus ingredientes para la pizza.")

        # Solicitar y validar el ingrediente proteico
        proteico = input("Ingrese el ingrediente proteico (pollo, vacuno, carne vegetal): ")
        if self.validar_elemento(proteico, self.ingredientes_proteicos):
            self.ingrediente_proteico = proteico
        else:
            print("Ingrediente proteico no válido.")
            return

        # Solicitar y validar los ingredientes vegetales
        vegetal1 = input("Ingrese el primer ingrediente vegetal (tomate, aceitunas, champiñones): ")
        if not self.validar_elemento(vegetal1, self.ingredientes_vegetales):
            print("Primer ingrediente vegetal no válido.")
            return
        self.primer_ingrediente_vegetal = vegetal1

        vegetal2 = input("Ingrese el segundo ingrediente vegetal (distinto al primero): ")
        if not self.validar_elemento(vegetal2, self.ingredientes_vegetales) or vegetal1 == vegetal2:
            print("Segundo ingrediente vegetal no válido o repetido.")
            return
        self.segundo_ingrediente_vegetal = vegetal2

        # Solicitar y validar el tipo de masa
        masa = input("Ingrese el tipo de masa (tradicional, delgada): ")
        if self.validar_elemento(masa, self.tipos_de_masa):
            self.tipo_de_masa = masa
        else:
            print("Tipo de masa no válido.")
            return

        self.es_valida = True
        print("Su pizza ha sido ordenada con éxito.")