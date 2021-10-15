import re

# pegar um e-mail com
# \w{5,50} username no mínimo 5 caracteres e no máximo 50 caracteres
# @ obrigatório
# \w{3,10} domínio com no mínimo 3 caracteres e no máximo 10 caracteres
# .(ponto) obrigatório e \w{2,3} .com
# .(ponto) obrigatório e \w{2,3} . br

padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "bla bla bla bla silvio@silvio.com.br wowoooo!!"
resposta = re.search(padrao, texto)
print(resposta.group())

#definir um padrão brasileiro com .br no final
padrao2 = "\w{5,50}@\w{3,10}.\w{2,3}.br"
texto2 = "bla bla bla bla nascimento@nascimento.com sales@sales.com.br wowoooo!!"
resposta2 = re.search(padrao2, texto2)
print(resposta2.group())

padrao_molde_tel = "(xx)aaaa-wwww"
padrao_tel = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
texto_tel = "número de telefone fixo 4126451234 celular 4199988877"
resposta_tel = re.findall(padrao_tel, texto_tel)
print(resposta_tel)