from calculo_soma import calcular_soma

def test_calcular_soma():
    assert calcular_soma(13) == 91
    assert calcular_soma(5) == 15
    assert calcular_soma(1) == 1
    assert calcular_soma(0) == 0
