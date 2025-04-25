import json
import os

def Limpar():
  os.system('cls')
Limpar()

with open("user-data.json", "r") as file:
  user_data = json.load(file)

print('💵 Seja bem-vindo ao ATM-Python 💵')

while True:
  user = str(input("Por favor, digite o seu usuário: "))
  password = str(input("Por favor, digite a sua senha: "))
  
  if user in user_data and user_data[user]["password"] == password:
    Limpar()
    print("✅ Login bem sucedido ✅")
    break
      
  else:
    Limpar()
    print("❌ Usuário ou senha incorretos. Tente novamente! ❌")