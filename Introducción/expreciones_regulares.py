import re

# validación de email
email = "mjt20@yavirac.com"
print(re.findall(r"\d", email))

print(bool(re.match(r"[\w.+-]+@[\w]+.[\d]", email)))
