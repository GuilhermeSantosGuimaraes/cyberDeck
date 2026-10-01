import json
import os
import time
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
    os.system('clear')

    print('\033[91m╔═════════════════════════════════════╗\033[0m')
    print('\033[91m║// MICROCYBER BATTLEDECK :: ADMIN [+]║\033[0m')
    print('\033[91m╠═════════════════════════════════════╣\033[0m')
    print('\033[91m║               RPG DECK              ║\033[0m')
    print('\033[91m╠═════════════════════════════════════╣\033[0m')
    print("\033[91m║  [ 1 ] :: GERAR_NOVO_REGISTRO       ║\033[0m")
    print("\033[91m║  [ 2 ] :: EXIBIR_DADOS_ATIVOS       ║\033[0m")
    print("\033[91m║  [ 3 ] :: ATUALIZAR_SINAIS_VITAIS   ║\033[0m")
    print("\033[91m║  [ 4 ] :: DESCONECTAR_SISTEMA       ║\033[0m")
    print("\033[91m║  [ 5 ] :: CARREGAR_ARQUIVO_LOCAL    ║\033[0m")
    print("\033[91m╚═════════════════════════════════════╝\033[0m")
    print("\033[91m:: STATUS: AGUARDANDO_INPUT // ■■■■■░░░░░ \033[0m")
    opcao = int(input('\033[91m >_ INSERIR_COMANDO: \033[0m'))

    if opcao < 1 or opcao > 5:
      print('\nNão é um opção valida')

    elif opcao == 1:
      ficha = Personagem.criar()
      salvar(ficha)
      time.sleep(2)

    elif opcao == 2:
      if ficha is None:
        print("\nNão existe ou nenhum ficha foi carregada")
        time.sleep(2)
      else:
        ficha.mostraPersonagem()
        input('\033[91m >_ APERTE_ENTER_PARA_CONTINUAR_<\033[0m')

    elif opcao == 3:
      if ficha is None:
        print("\nNão existe ou nenhum ficha foi carregada")
        time.sleep(2)
      else:
        ficha.alteraPV()
        salvar(ficha)

    elif opcao == 4:
        if ficha is None:
          print("Tchau...")  
        else:
          salvar(ficha)
          print('Ficha Salva!')
          print("Tchau...")

    elif opcao == 5:
      arquivo, msg = carregar()
      if msg == 'sucesso':
        ficha = arquivo
        print('Ficha Carregada')
        time.sleep(2)
      elif msg == 'nenhuma ficha salva':
        print(msg)
        time.sleep(2)
      elif msg == 'arquivo corrompido':
        print('Ficha corrompida')
        time.sleep(2)
      elif msg == 'Não existe fichas de personagem salvas':
        print('Não existe fichas de personagem salvas')
        time.sleep(2)

