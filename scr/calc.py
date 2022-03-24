def get_fractions(valor):
  if("/" in valor):
    decimal = int (valor[0:1]) / int (valor[2:3])
    return decimal
  else:
    return float(valor)

def suma(a,b):
  sumandoa = get_fractions(a)
  sumandob = get_fractions(b)
  return sumandoa + sumandob