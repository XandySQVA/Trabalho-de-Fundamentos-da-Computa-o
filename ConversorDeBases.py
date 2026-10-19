numeroDecimal = int(input("Digite um número decimal: "))
opcao = int(input("2 para binário, 8 para octal e 16 para Hexadecimal: "))
resto = []

while numeroDecimal > 0:
  numeroConvertido = numeroDecimal%opcao
  if numeroConvertido == 10:
    resto.insert(0, "A")
  elif numeroConvertido == 11:
    resto.insert(0, "B")
  elif numeroConvertido == 12:
    resto.insert(0, "C")
  elif numeroConvertido == 13:
    resto.insert(0, "D")
  elif numeroConvertido == 14:
    resto.insert(0, "E")
  elif numeroConvertido == 15:
    resto.insert(0, "F")
  else:
    resto.insert(0, numeroConvertido)
  numeroDecimal //= opcao
print(resto)
