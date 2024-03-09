from TelefoneBR import TelefonesBR

numero = "11627289456"
numero_objeto = TelefonesBR(numero)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

print(numero_objeto)