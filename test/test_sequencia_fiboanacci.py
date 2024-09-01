from sequencia_fibonacci import pertence_fibonacci

def test_pertence_fibonacci():
    assert pertence_fibonacci(0) == True
    assert pertence_fibonacci(1) == True
    assert pertence_fibonacci(2) == True
    assert pertence_fibonacci(3) == True
    assert pertence_fibonacci(5) == True
    assert pertence_fibonacci(8) == True
    assert pertence_fibonacci(13) == True
    assert pertence_fibonacci(4) == False
    assert pertence_fibonacci(6) == False
    assert pertence_fibonacci(7) == False
