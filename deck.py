import json
  
def criaPersonagem():
    personagem = {
          'nome': input('Digite o nome: '),
          'classe': input('Digite a classe: '),
          'nivel': int(input('Digite o nivel do personagem: ')),
          'PV Maximo': int(input('Digite o PV Máximo: ')),
          'PV Atual': int(input('Digite o PV Atual: ')),
          'atributos': {
              'Força': int(input('Digite a valor da Força do personagem: ')),
              'Destreza': int(input('Digite a valor da Destreza do personagem: ')),
              'Constituição': int(input('Digite a valor da Constituição do personagem: ')),
              'Inteligencia': int(input('Digite a valor da Inteligencia do personagem: ')),
              'Sabedoria': int(input('Digite a valor da Sabedoria do personagem: ')),
              'Carisma': int(input('Digite a valor do Carisma do personagem: '))
          },
        }
    return personagem

def mostraPersonagem(personagem):
  print('\n================================')
  print('           RPG DECK             ')
  print('================================')

  print(f'\nNome: {personagem['nome']}')
  print(f'Classe: {personagem['classe']}')
  print(f'Nível: {personagem['nivel']}')

  print(f'\nPV: {personagem['PV Atual']}/{personagem['PV Maximo']}')

  print('\n-------- ATRIBUTOS -----------\n')

  for atributos in personagem['atributos']:
    print(f"{atributos}: {personagem['atributos'][atributos]}")

def alteraPV(personagem):
  print('\n1 - Aumentar vida Atual')
  print('2 - Diminuir vida Atual')
  print('3 - Aumentar vida Máxima')
  print('4 - Diminuir vida Máxima')
  opcao = int(input('Digite a sua opção: '))

  if opcao < 1 or opcao > 4:
    print('Opção inválida')
  elif opcao == 1:
    valor = int(input("Digite quanto de cura seu personagem recebeu: "))
    personagem['PV Atual'] += valor
  elif opcao == 2:
    valor = int(input("Digite quanto de dano seu personagem recebeu: "))
    valorNovo = personagem['PV Atual'] - valor
    if valorNovo <= 0:
      personagem['PV Atual'] = 0
    else:
      personagem['PV Atual'] = valorNovo
  elif opcao == 3:
    valor = int(input("Digite quanto de PV Máxima aumenta: "))
    personagem['PV Maximo'] += valor
  elif opcao == 4:
    valor = int(input("Digite quanto de PV Máxima diminuiu: "))
    valorNovo = personagem['PV Maximo'] - valor
    if valorNovo <= 0:
      personagem['PV Maximo'] = 0
    else:
      personagem['PV Maximo'] = valorNovo

  return personagem

def salvar(personagem):
  ficha = open("personagem.json", "w")
  json.dump(personagem, ficha)
  ficha.close()

def carregar():
  try:
    with open("personagem.json", "r") as ficha:
      personagem = json.load(ficha)
    return (personagem, 'sucesso')
  except FileNotFoundError:
    return (None, 'nenhuma ficha salva')
  except json.JSONDecodeError:
    return (None, 'arquivo corrompido')

def menu():
  personagem = None
  opcao = None
  while opcao != 4:
    print('\n================================')
    print('           RPG DECK             ')
    print('================================')

    print('\n1 - Criar personagem')
    print('2 - Mostrar personagem')
    print('3 - Alterar PV')
    print('4 - Sair')
    print('5 - Carregar Personagem')
    opcao = int(input('Escolha uma opção: '))

    if opcao < 1 or opcao > 5:
      print('\nNão é um opção valida')
    elif opcao == 1:
      personagem = criaPersonagem()
      salvar(personagem)
    elif opcao == 2:
      if personagem is None:
        print("\nNão existe personagem criados")
      else:
        mostraPersonagem(personagem)
    elif opcao == 3:
      if personagem is None:
        print("\nNão existe personagem criados")
      else:
        alteraPV(personagem)
        salvar(personagem)
    elif opcao == 4:
      if personagem is None:
        print("\nTchau...")
      else:
        salvar(personagem)
        print("\nAlterações salvas")
        print("Tchau...")
    elif opcao == 5:
      ficha, msg = carregar()
      if msg == 'sucesso':
        personagem = ficha
        print('Personagem salvo com sucesso')
      elif msg == 'nenhuma ficha salva':
        print(msg)
      elif msg == 'arquivo corrompido':
        print('Ficha corrompida')


