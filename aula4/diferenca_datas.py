from datetime import datetime, timedelta
from datas_br import DatasBr

#hoje = datetime.today()
#amanha = datetime.today() + timedelta(days=1, hours=20)

#print(hoje - amanha)

hoje = DatasBr()
print(hoje.tempo_cadastro())