
def validate_number (mensaje_error: str,numero: int,min: int,max: int,intentos: int) -> int|None:
    """valida que el dato que ingreso el usuario sea un numero y que este dentro del rango indicado

    Args:
        mensaje_error (str): mensaje que se mostrara al usuario en caso de que el dato ingresado no cumpla con los parametros indicados para pasar la validacion
        numero (int): input del usuario
        min (int): numero minimo admitido
        max (int): numero maximo admitido
        intentos (int): cantidad de intentos para ingresar un dato

    Returns:
        int|None: retorna un numero entero en caso de ingresarse un numero valido en la cantidad de intentos permitidos, de lo contrario retorna None
    """
    vuelta = 0
    while True:
        if vuelta > 0:
            numero = input(f"{mensaje_error}le quedan {intentos} intentos: ")
        try:
            if float(numero) >= min and float(numero) <= max :
                return float(numero)
        except:
            pass
        intentos -= 1
        if intentos == 0:
            return None
        vuelta +=1
    
def validate_lenght (cadena: str, longitud: int) -> str:
    """verifica la longitud de la cadena enviada por parametro

    Args:
        cadena (str): cadena de texto a verificar
        longitud (int): longitud de caracteres que debe tener el texto

    Returns:
        str: devuelve la cadena verificada
    """
    while len(cadena) != longitud:
        cadena = str(input(f"La cadena ingresada no cumple con los parametros dados, pruebe denuevo, recuerde que la longitud debe ser de {longitud} caracteres: "))
    return cadena