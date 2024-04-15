import pytest
from main import media

def test_lista_vazia():
    result = media([])
    assert result == 0
    
def test_lista_com_um_elemento():
    result = media([5])
    assert result == 5
    
def test_lista_com_dois_elementos():
    result = media([5, 7])
    assert result == 6

def test_resultado_float():
    result = media([5, 2])
    assert result == 3.5
    assert type(result) == float
    
def test_lista_com_elementos_negativos():
    result = media([-5, -7, -10])
    assert result == -7.333333333333333
    
def test_lista_com_multiplos_elementos():
    resultado = media([1, 2, 3, 4, 5])
    assert resultado == 3
