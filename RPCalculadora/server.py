from xmlrpc.server import SimpleXMLRPCServer

def add_numbers(a, b):
    return a + b


def rest_numbers(a,b):
    return a -b

def mult_numbers(a,b):
    return a  * b

def div_numbers(a, b):
        if b == 0:
            return "Error al dividir "
        return a / b



server = SimpleXMLRPCServer(('localhost', 9000))
print("Listening on port 9000...")
server.register_function(add_numbers, 'add')
server.register_function(rest_numbers, 'rest')
server.register_function(mult_numbers, 'multi')
server.register_function(div_numbers, 'div')



server.serve_forever()
