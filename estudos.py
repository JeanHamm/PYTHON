from conta import Conta

conta1 = Conta( 123, "Jean", 100.00, 2500.00)
conta2 = Conta( 321, "Nico", 0, 45034.00)
conta3 = Conta( 425, "Steffany", 1020.00, 12011.00)



conta1.transferir(conta2, 100.01)

conta1.extrato()
conta2.extrato()

conta3.set_limite(250.00)
print(conta3.get_limite())