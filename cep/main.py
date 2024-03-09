import requests
from acesso_cep import BuscaEndereco
cep = "02536110"
objeto_cep = BuscaEndereco(cep)

rua, bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(f"""
      Logradouro: {rua}
      Bairro: {bairro} 
      Cidade: {cidade}
      UF: {uf}
""")