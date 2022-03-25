'<<<<<<< HEAD'


def get_fractions(valor):

    """

    Args:
      valor: recive un valor numérico (acepta fracciones) 

    Returns: regresa los valores en valores tipo flotante

    """
    numero = 0
    try:
        if(isinstance(valor,str)):
            print(valor)
            if "/" in valor :
                arr = valor.split("/")
                numerador = arr[0]
                denominador = arr[1]
                numero = float(numerador) / float(denominador)
        else:
            numero = float(entrada)
            print(type(numero))
      
         if(isinstance(entrada,int) or  isinstance(entrada,float)):
             numero = entrada
    except:
        print("Error de formato de numero")
    return numero


def suma(a, b):
    """

    Args:
      a: representa el primer sumando
      b: represenra el segundo sumando

    Returns: regresa la suma del primer sumando y el segundo sumando

    """
    sumandoa = get_fractions(a)
    sumandob = get_fractions(b)
    return sumandoa + sumandob


'#======='


def multiplica(a, b):
    """

    Args:
      a: representa el multiplicando
      b: representa el multiplicador

    Returns: regresa la multiplicación del muntiplicando por el multiplicador

    """
    multiplicando = get_fractions(a)
    multiplicador = get_fractions(b)
    return multiplicando * multiplicador


'#>>>>>>> mult'
