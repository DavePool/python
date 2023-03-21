#!/bin/python
class cuenta(object):
    """docstring for cuenta."""
    def __init__(self, numeroDeCuenta, titular, saldo):
        super(cuenta, self).__init__()
        self.numeroDeCuenta = numeroDeCuenta
        self.titular = titular
        self.saldo = saldo

    def realizarRetiro(retiro):
        if retiro < 0:
            print "Operacion no valida"
        else:
            saldo -= retiro;
            print "operacion exitosa, saldo actual es de: "+ saldo
        pass

cuenta1 = cuenta(232244,"DavePool", 234)
cuenta.realizarRetiro(230)
