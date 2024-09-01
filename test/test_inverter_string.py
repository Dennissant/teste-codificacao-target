from inverter_string import inverter_string

def test_inverter_string():
    assert inverter_string("Alice") == "ecilA"
    assert inverter_string("Python") == "nohtyP"
    assert inverter_string("12345") == "54321"

    assert inverter_string("") == ""
