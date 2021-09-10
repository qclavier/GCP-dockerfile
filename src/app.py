def maj_letter(mot):
    return str.capitalize(mot[0])


def test_maj_letter():
    test = maj_letter("Quentin")
    assert test == "Q"