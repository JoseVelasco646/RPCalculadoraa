import xmlrpc.client

def main():
    proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")
    
    while True:
        print("Elige una operación:")
        print("1: Sumar")
        print("2: Restar")
        print("3: Multiplicar")
        print("4: Dividir")
        print("5: Salir")
        
        opc = input("Ingresa tu elección (1/2/3/4/5): ")
        
        if opc == '5':
            print("Saliendo...")
            break
        
        if opc in ['1', '2', '3', '4']:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            
            if opc == '1':
                result = proxy.add(a, b)
                print("Resultado de {} + {} es: {}".format(a, b, result))
            elif opc == '2':
                result = proxy.rest(a, b)
                print("Resultado de {} - {} es: {}".format(a, b, result))
            elif opc == '3':
                result = proxy.multi(a, b)
                print("Resultado de {} * {} es: {}".format(a, b, result))
            elif opc == '4':
                result = proxy.div(a, b)
                print("Resultado de {} / {} es: {}".format(a, b, result))
        else:
            print("Elección no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
