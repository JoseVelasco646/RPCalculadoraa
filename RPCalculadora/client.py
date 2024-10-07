import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")
result = proxy.add(2, 3)
print("Result of 2 + 3 is:", result)

result = proxy.rest(2, 3)
print("Result of 2 - 3 is:", result)

result = proxy.multi(2, 3)
print("Result of 2 * 3 is:", result)

result = proxy.div(2, 10)
print("Result of 2 / 10 is:", result)
 