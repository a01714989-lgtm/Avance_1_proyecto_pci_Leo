#Importamos la libreria math para realizar diferentes operaciones matematicas
import math

def buscar_en_matriz(codigo_producto, matriz):
    for fila in matriz:
        if fila[0] == codigo_producto:
            return fila  # Retorna la lista del producto encontrado
    return None

#FUNCION DE BUSQUEDA DE PORDUCTOS

def productos_busqueda(codigo_producto):

    #CICLO DE BUSQUEDA DE LOS PRODUCTO

    while True:
        
        producto = buscar_en_matriz(codigo_producto, matriz_producto)

        if producto:
            cantidad = int(input("\nDigite la cantidad de productos: "))
            print("\nProducto:", producto[1], " Cantidad:", cantidad, " Precio Unitario: $", producto[2])
            subtotal = producto[2] * cantidad
        else:
            print("\nEl código no coincide con ningún producto\n")
            break

        dc = input("\n¿Desea añadir otro producto? (Si/No): ")
        
        if dc.lower() == "no":
            break
        
        codigo_producto = int(input("\nDigite el codigo del producto: "))

    print("El subtotal es: $", subtotal)

    # Cálculo del IVA
    iva = subtotal * 0.16

    # Cálculo de factura total
    total_factura = subtotal + iva

    print("\nIVA: $", iva, "\nTotal: $", total_factura)


#Establecemos los productos disponibles(listas)

producto_1 = [1234567890123, "Sandwich Helado Clasico", 28]

producto_2 = [4829301756248, "Takis Fuego Morados", 25.5]

producto_3 = [7601938421576, "Chokis Rojas", 20.5]

producto_4 = [5092846173921, "Electrolit lima limon", 32.5]

producto_5 = [1837562094853, "Trident Negros chicles", 18]

#Establecemos la matriz

matriz_producto = [
    producto_1,
    producto_2,
    producto_3,
    producto_4,
    producto_5
]

#Establecemos el parametro para la funcion

codigo_producto = int(input("\nDigite el codigo del producto: "))


#Llamamos a la funcion incluyendo el parametro selecionado
productos_busqueda(codigo_producto)
