from conta import Conta

conta1 = Conta( 123, "jean", 100.00, 2500.00)
conta2 = Conta( 321, "Nico", 0, 45034.00)
conta3 = Conta( 425, "Steffany", 1020.00, 12011.00)

conta1.extrato()
conta1.saca(50.00)
conta1.extrato()
conta1.saca(50.00)
conta1.extrato()
conta1.saca(50.00)
conta1.extrato()

codigos = Conta.codigo_dos_bancos()

print(codigos["Stone"])