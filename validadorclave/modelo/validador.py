# TODO: Implementa el código del ejercicio aquí


from .errores import (
    NoCumpleLongitudMinimaError,
    NoTieneLetraMayusculaError,
    NoTieneLetraMinusculaError,
    NoTieneNumeroError,
    NoTieneCaracterEspecialError,
    NoTienePalabraSecretaError
)

class ReglaValidacion:
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise NoCumpleLongitudMinimaError(f"La clave debe tener una longitud de más de {self._longitud_esperada} caracteres")

    def _contiene_mayuscula(self, clave):
        if not any(c.isupper() for c in clave):
            raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")

    def _contiene_minuscula(self, clave):
        if not any(c.islower() for c in clave):
            raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minúscula")

    def _contiene_numero(self, clave):
        if not any(c.isdigit() for c in clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave):
        caracteres_especiales = '@_#$%'
        if not any(c in caracteres_especiales for c in clave):
            raise NoTieneCaracterEspecialError("La clave debe contener al menos un carácter especial (@, _, #, $, %)")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave):
        mayusculas_calisto = sum(1 for c in clave if c in "CALISTO")
        if mayusculas_calisto < 2 or mayusculas_calisto == len("calisto"):
            raise NoTienePalabraSecretaError("La palabra 'calisto' debe estar escrita con al menos dos letras en mayúscula")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_numero(clave)
        self.contiene_calisto(clave)
        return True

class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        return self.regla.es_valida(clave)
