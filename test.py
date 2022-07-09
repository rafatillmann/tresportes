numbers = "15.703.598/0001-52"

values = [char for char in numbers if char.isdigit()]
cnpj = int(''.join(values))
print(cnpj)
