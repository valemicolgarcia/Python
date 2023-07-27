import re

email = "example@example.com"

#el + nos busca 1 o + coincidencias
pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" #ejemplo [vale] [@gmail] [.] [com]

result = re.match(pattern, email)

if result:
    print ("direccion de correo valida")
else:
    print ("direccion de correo invalida")