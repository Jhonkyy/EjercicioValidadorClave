from abc import ABC, abstractmethod
from .errores import (
    NoCumpleLongitudMinimaError,
    NoTieneLetraMayusculaError,
    NoTieneLetraMinusculaError,
    NoTieneNumeroError,
    NoTieneCaracterEspecialError,
    NoTienePalabraSecretaError
)

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise NoCumpleLongitudMinimaError(f"La clave debe tener una longitud de más de {self._longitud_esperada} caracteres")
        return True

    def _contiene_mayuscula(self, clave):
        if not any(c.isupper() for c in clave):
            raise NoTieneLetraMayusculaError("La clave debe tener al menos una letra mayúscula")
        return True

    def _contiene_minuscula(self, clave):
        if not any(c.islower() for c in clave):
            raise NoTieneLetraMinusculaError("La clave debe tener al menos una letra minúscula")
        return True

    def _contiene_numero(self, clave):
        if not any(c.isdigit() for c in clave):
            raise NoTieneNumeroError("La clave debe tener al menos un número")
        return True

    @abstractmethod
    def es_valida(self, clave):
        pass

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave):
        especiales = {'@', '_', '#', '$', '%'}
        if not any(c in especiales for c in clave):
            raise NoTieneCaracterEspecialError("La clave debe tener al menos un caracter especial (@, _, #, $, %)")
        return True

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
        palabra = "calisto"
        idx = clave.lower().find(palabra)
        if idx == -1:
            raise NoTienePalabraSecretaError("La clave debe contener la palabra 'calisto'")

        substring = clave[idx:idx+len(palabra)]
        mayusculas = sum(1 for c in substring if c.isupper())

        if mayusculas < 2 or mayusculas == len(palabra):
            raise NoTienePalabraSecretaError("La palabra calisto debe estar escrita con al menos dos letras en mayúscula pero no todas")
        return True

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
