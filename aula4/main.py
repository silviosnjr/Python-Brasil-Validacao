from datetime import datetime, timedelta
from datas_br import DatasBr

cadastro = DatasBr()
#print(cadastro.momento_cadastro)
#print(cadastro.mes_cadastro())
#print(cadastro.dia_semana())
print(cadastro.format_data())


#hoje = datetime.today()
#hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")
#print(hoje_formatada)