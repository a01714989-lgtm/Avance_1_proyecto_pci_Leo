def buscar_en_matriz(codigo_producto, matriz):
    """Busca un producto en matriz por su código y retorna su información."""
    for fila in matriz:
        if fila[0] == codigo_producto:
            return fila
    return None


def productos_busqueda(codigo_producto):
    """Procesa la compra de productos y calcula el subtotal, IVA y total."""
    subtotal = 0
    
    while True:
        producto = buscar_en_matriz(codigo_producto, matriz_producto)

        if producto:
            cantidad = int(input("\nDigite la cantidad de productos: "))
            print("\nProducto:", producto[1], " Cantidad:", cantidad,
                  " Precio Unitario: $", producto[2])
            subtotal += producto[2] * cantidad
            desea_continuar = input("\n¿Desea añadir otro producto? (Si/No): ")
            if desea_continuar.lower() == "no":
                break
        else:
            print("\nEl código no coincide con ningún producto\n")

        codigo_producto = int(input("\nDigite el codigo del producto: "))

    print("El subtotal es: $", subtotal)

    iva = subtotal * 0.16
    total_factura = subtotal + iva

    print("\nIVA: $", iva, "\nTotal: $", total_factura)


producto_1 = [1234567890123, "Sandwich Helado Clasico", 28]
producto_2 = [4829301756248, "Takis Fuego Morados", 25.5]
producto_3 = [7601938421576, "Chokis Rojas", 20.5]
producto_4 = [5092846173921, "Electrolit lima limon", 32.5]
producto_5 = [1837562094853, "Trident Negros chicles", 18]

matriz_producto = [
    producto_1,
    producto_2,
    producto_3,
    producto_4,
    producto_5
]

codigo_producto = int(input("\nDigite el codigo del producto: "))

productos_busqueda(codigo_producto)