import json
import os

class Personagem:
  def __init__(self, nome, classe, nivel, pvMax, pvAtual, atributos):
    self.nome = nome
    self.classe = classe
    self.nivel = nivel
    self.pvMax = pvMax
    self.pvAtual = pvAtual
    self.atributos = atributos

  @classmethod
  def criar(cls):
    nome = input('Digite o nome: ')
    classe = input('Digite a classe: ')
    nivel = int(input('Digite o nivel do personagem: '))
    pvMax = int(input('Digite o PV Máximo: '))
    pvAtual = int(input('Digite o PV Atual: '))
    atributos = {
      'Força': int(input('Digite a valor da Força do personagem: ')),
      'Destreza': int(input('Digite a valor da Destreza do personagem: ')),
      'Constituição': int(input('Digite a valor da Constituição do personagem: ')),
      'Inteligencia': int(input('Digite a valor da Inteligencia do personagem: ')),
      'Sabedoria': int(input('Digite a valor da Sabedoria do personagem: ')),
      'Carisma': int(input('Digite a valor do Carisma do personagem: '))
    }
    
    return cls(nome, classe, nivel, pvMax, pvAtual, atributos)

  def mostraPersonagem(self):
    print('\n================================')
    print('           RPG DECK             ')
    print('================================')

    print(f'\nNome: {self.nome}')
    print(f'Classe: {self.classe}')
    print(f'Nível: {self.nivel}')

    print(f'\nPV: {self.pvAtual}/{self.pvMax}')

    print('\n-------- ATRIBUTOS -----------\n')

    for atributos, valores in self.atributos.items():
      print(f"{atributos}: {valores}")

  def alteraPV(self):
    print('\n1 - Aumentar vida Atual')
    print('2 - Diminuir vida Atual')
    print('3 - Aumentar vida Máxima')
    print('4 - Diminuir vida Máxima')
    opcao = int(input('Digite a sua opção: '))

    if opcao < 1 or opcao > 4:
      print('Opção inválida')
    elif opcao == 1:
      valor = int(input("Digite quanto de cura seu personagem recebeu: "))
      self.pvAtual += valor
    elif opcao == 2:
      valor = int(input("Digite quanto de dano seu personagem recebeu: "))
      valorNovo = self.pvAtual - valor
      if valorNovo <= 0:
        self.pvAtual = 0
      else:
        self.pvAtual = valorNovo
    elif opcao == 3:
      valor = int(input("Digite quanto de PV Máxima aumenta: "))
      self.pvMax += valor
    elif opcao == 4:
      valor = int(input("Digite quanto de PV Máxima diminuiu: "))
      valorNovo = self.pvMax - valor
      if valorNovo <= 0:
        self.pvMax = 0
      else:
        self.pvMax = valorNovo

  def para_dict(self):
    personagem = {
      'nome': self.nome,
      'classe': self.classe,
      'nivel': self.nivel,
      'PV Maximo': self.pvMax,
      'PV Atual': self.pvAtual,
      'atributos': self.atributos
    }

    return personagem

  @classmethod
  def de_dict(cls, dados):
    nome = dados['nome']
    classe = dados['classe']
    nivel = dados['nivel']
    pvMax = dados['PV Maximo']  
    pvAtual = dados['PV Atual']
    atributos = dados['atributos']

    return cls(nome, classe, nivel, pvMax, pvAtual, atributos)
    
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


menu()