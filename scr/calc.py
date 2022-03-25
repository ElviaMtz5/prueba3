'#<<<<<<< HEAD'


def get_fractions(valor):
    """
    Descripción: Esta fucnión recibe un "valor" en forma de 
    fracción el cual convierte a decimal 
    """
    if("/" in valor):
        decimal = int(valor[0:1]) / int(valor[2:3])
        return decimal
    else:
        return float(valor)


def suma(a, b):
    """
    Descripción: Esta fucnión recibe dos valores los cuales pueden ser fracciones,
    dichos valores serán sumados 

    Parametrers:
        a - es el primer sumando
        b - es el segundo sumando 

    Returns
        Regresa la suma del primer sumando más el segundo sumando
    """


    sumandoa = get_fractions(a)
    sumandob = get_fractions(b)
    return sumandoa + sumandob


'#======='


def multiplica(a, b):
    """
    Descripción: Esta fucnión recibe dos valores los cuales pueden ser valores en fracciones,
    dichos valores serán multiplicados

    Parametrers:
        a - es el multiplicando
        b - es el multiplicador 

    Returns
        Regresa la multiplicación del multiplicando y el multiplicador
    """


    multiplicando = get_fractions(a)
    multiplicador = get_fractions(b)
    return multiplicando * multiplicador


'#>>>>>>> mult

pip install pyment