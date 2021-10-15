import requests
from acesso_cep import BuscaEndereco

cep = 80210390
objeto_cep = BuscaEndereco(cep)
#print(objeto_cep.format_cep())

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)
