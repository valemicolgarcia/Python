
#condicionales

#IF / ELSE --------------------------------
edad = 20
if edad >= 18:
    print ("Podes pasar")
    print ("holis!!!!")
else:
    print ("No podes pasar")
    print ("chau")

#ELSE / IF --------------------------------
num = 10000000
if (num > 10000):
    print("VIP")
elif (num > 1000):       #else if --> elif
    print ("NORMAL")
else: print ("NO ENTRA")

#IF ANIDADOS--------------------------
if (num > 10000):
    print ("VIPPPPP")
    if (num >20000):
        print ("HOLA")
    else:
        print ("CHAU")
        
elif (num > 10):
    print ("normal")
else: print ("NO ENTRA")


