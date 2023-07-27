import re

text = "The quick brown fox jumps over the lazy dog"

#el asterisco * afecta al operador anterior
# * --> encuentra 0 coincidencias o alguna
x = re.search("^The.*dog$", text)
if x:
    print ("SI")
else:
    print ("NO")