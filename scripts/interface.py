import json
import os
from personagem import Personagem

def salvar(personagem):
  dicionario = personagem.para_dict()
  with open(f"{dicionario['nome']}.json", "w") as ficha:
    json.dump(dicionario, ficha, ensure_ascii=False)

def carregar():
  listaJson = []
  listaDir = os.listdir()
  for arquivo in listaDir:
    if arquivo.endswith('.json'):
      listaJson.append(arquivo)

  if listaJson == []:
    return (None,'Não existe fichas de personagem salvas')
  else:
    for i, nome in enumerate(listaJson):
      print(f"{i} - {nome.replace('.json', '')}")

    escolha = int(input("Qual ficha você quer abrir: "))
    personagem = listaJson[escolha]

    try:
      with open(f"{personagem}", "r") as ficha:
        personagem = json.load(ficha)
        arquivo = Personagem.de_dict(personagem)
      return (arquivo, 'sucesso')
    except FileNotFoundError:
      return (None, 'nenhuma ficha salva')
    except json.JSONDecodeError:
      return (None, 'arquivo corrompido')

def menu():
  ficha = None
  opcao = None
  while opcao != 4:
    print('\n================================')
    print('           RPG DECK             ')
    print('================================')

    print('\n1 - Criar ficha')
    print('2 - Mostrar ficha')
    print('3 - Alterar PV')
    print('4 - Sair')
    print('5 - Carregar ficha')
    opcao = int(input('Escolha uma opção: '))

    if opcao < 1 or opcao > 5:
      print('\nNão é um opção valida')

    elif opcao == 1:
      ficha = Personagem.criar()
      salvar(ficha)

    elif opcao == 2:
      if ficha is None:
        print("\nNão existe ou nenhum ficha foi carregada")
      else:
        ficha.mostraPersonagem()

    elif opcao == 3:
      if ficha is None:
        print("\nNão existe ou nenhum ficha foi carregada")
      else:
        ficha.alteraPV()
        salvar(ficha)

    elif opcao == 4:
        salvar(ficha)
        print('Ficha Salva!')
        print("Tchau...")

    elif opcao == 5:
      arquivo, msg = carregar()
      if msg == 'sucesso':
        ficha = arquivo
        print('Ficha Carregada')
      elif msg == 'nenhuma ficha salva':
        print(msg)
      elif msg == 'arquivo corrompido':
        print('Ficha corrompida')
      elif msg == 'Não existe fichas de personagem salvas':
        print('Não existe fichas de personagem salvas')

