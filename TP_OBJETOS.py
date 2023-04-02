'''1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
del rectángulo.'''

# class Rectangulo:

   

#     def __init__(self, base, altura):
#         self.Base=base
#         self.Altura=altura

#     def Area(self):
#         return self.Base*self.Altura


# Rect1=Rectangulo(2,12)
# print(Rect1.Area())            


'''Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.'''

# class Mate:
#     Cebadas=8
#     Estado='Lleno'
#     n=13

#     def __init__(self, cebadas, estado,cebadas_max):
#         self.Cebadas=cebadas
#         self.Estado=estado
#         self.n=cebadas_max

#     def Cebar(self):
#         if self.Estado=="vacio":
#             print(f'Su mate esta lleno')
#         else:
#             self.Estado=='lleno'
#             print('¡Cuidado! ¡Te quemaste!')


#     def Beber(self):
#         self.Estado='Vacio'
#         self.Cebadas-=1

#     def Mate_Lavado(self):
#         if self.Cebadas==0:
#             print('El mate esta lavado')



# mate1=Mate('Lleno', 8, 8 )
# print(mate1.Beber)



'''corchos'''

class Corcho:
    def __init__(self, Bodega):
        self.Bodega=Bodega

class Botella:
    def __init__(self, Corcho:Corcho):
        self.CorchoDeBotella=Corcho


class Saca_Corcho:
    def __init__(self):
        self.CorchoSacado=None

    def Destapar(self, Botella:Botella):
        self.CorchoSacado=Botella.CorchoDeBotella
        Botella.CorchoDeBotella=None

    def Limpiar(self):
        self.CorchoSacado=None    







        

    


    


        
