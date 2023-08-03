from datetime import datetime, timezone, timedelta

data_e_hora_atual = datetime.now()

data_e_hora_em_texto = data_e_hora_atual.strftime('%d/%m/%Y %H:%M')

data_e_hora = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M')

diferença = timedelta(hours= -3)
fuso_horario = timezone(diferença)
print(fuso_horario)

data_e_hora_são_paulo = data_e_hora_atual.astimezone(fuso_horario)

data_e_hora_são_paulo = data_e_hora_são_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_são_paulo)