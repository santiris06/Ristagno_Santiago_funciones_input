from Validate import validate_lenght, validate_number

attempts = 5
longitud = 6
minimo = 10
maximo = 100
msj = f"Ingrese un numero entre {minimo} y {maximo}: "
msj_error = "El dato ingresado no es valido, "

def get_int (mensaje: str)-> int|None:
    """Pide un numero entero al usuario

    Args:
        mensaje (str): mensaje que se va a mostrar al usuario al pedir el numero por primera vez

    Returns:
        int|None: retorna un numero entero en caso de ingresarse un numero valido en la cantidad de intentos permitidos, de lo contrario retorna None
    """
    numero = input(mensaje)
    return int(validate_number (msj_error,numero,minimo,maximo,(attempts+1)))

def get_float (mensaje: str) -> float|None:
    """pide un numero al usuario (float o int)

    Args:
        mensaje (str): mensaje que se va a mostrar al usuario al pedir el numero por primera vez

    Returns:
        float|None: retorna un numero entero o float en caso de ingresarse un numero valido en la cantidad de intentos permitidos, de lo contrario retorna None
    
    """
    numero = input(mensaje)
    return float(validate_number (msj_error, numero, minimo, maximo, (attempts+1)))

def get_string (longitud: int) -> str:
    """pide un string al usuario para ser verificado

    Args:
        longitud (int): longitud de caracteres que debe tener el texto

    Returns:
        str: retorna la cadena en caso de tener la longitud deseada
    """
    cadena = str(input(f"Ingrese un texto de una longitud de {longitud} caracteres: "))
    return validate_lenght(cadena,longitud)   

print(get_int(msj))
print(get_float(msj))
print(get_string(longitud))