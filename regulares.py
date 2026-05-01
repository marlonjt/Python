import re

txt = "Python es un lenguaje bueno de aprender porque es algo nuevo y es usado mucho"


print(re.search("aprender", txt))
print(re.findall("es", txt))
print(re.search("aprender", txt).start())
print(re.search("aprender", txt).end())
print(re.search("aprender", txt).span())

lista_re = ["mujeres", "hombres", "niños", "niñas"]

for elemento in lista_re:
    if re.findall("niñ[oa]s", elemento):
        print(elemento)
