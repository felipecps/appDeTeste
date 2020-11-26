from validate_docbr import CPF


def testeCPF():
    cpf = CPF()
    # Validar CPF
    if cpf.validate("012.345.67d-90"):  # True
        return 'sim'
    else:
        return 'nao'
    #print(cpf.validate("012.345.678-91"))  # False