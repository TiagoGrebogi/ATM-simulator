import json
import os
import sys

with open("user-data.json", "r") as file:
  user_data = json.load(file)
  
def Limpar():
  os.system('cls')
Limpar()

attemp = 3
def Login(user, password):
  if user in user_data and user_data[user]["password"] == password:
    print("✅ Login bem sucedido ✅")
    return True
    
  else:
    global attemp
    attemp -= 1
    print(f"❌ Usuário ou senha incorretos. Você tem apenas mais {attemp} tentativas. Tente novamente! ❌")
    return False

def CheckBalance(user):
  return print(f"O saldo do usúario {user_data[user]["nickname"]} é de R${user_data[user]["balance"]}")

def DepositMoney(amount):
  user_data[user]["balance"] += amount
  with open ("user-data.json", "w") as file:
    json.dump(user_data, file, indent=2)
    
  return print(f"O valor de R${amount} foi inserido com sucesso!")

def DrawMoney(amount):
  ...

print('💵 Seja bem-vindo ao ATM-Python 💵')

while True: # verifying login
  user = str(input("Por favor, digite o seu usuário: "))
  password = str(input("Por favor, digite a sua senha: "))
  Limpar()
  
  
  if Login(user, password):
    break

  if attemp == 0: # will verifies if the usuarie tried to acess 3 times
    Limpar()
    print("❌ Você tentou muitas vezes! Aguarde um instante e tente novamente. ❌")
    sys.exit()
  
while True:
  main_options = int(input("""Oque você deseja fazer?
      
1 - Consultar Saldo
2 - Depositar Dinheiro
3 - Sacar Dinheiro
4 - Sair do Sistema
"""))
  
  Limpar()
  
  if main_options == 1:
    CheckBalance(user)
    
  elif main_options == 2:
    Limpar()
    
    amount = float(input("Qual o valor deseja inserir?"))
    DepositMoney(amount)
    
  elif main_options == 3:
    ...
    
  elif main_options == 4:
    sys.exit()
    
  else:
    print("Você digitou uma opção inválida. Por favor, tente novamente!")
    continue