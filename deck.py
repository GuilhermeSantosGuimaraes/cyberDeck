import json
import os

class Personagem:
  def __init__(self, nome, classe, raca, nivel, pvMax, pvAtual, atributos, ca, antecedente, deslocamento, itens = None, magias = None, truques = None):
    self.nome = nome
    self.classe = classe
    self.nivel = nivel
    self.raca = raca
    self.pvMax = pvMax
    self.pvAtual = pvAtual
    self.atributos = atributos
    self.bonusProf = ((self.nivel - 1) // 4) + 2
    self.ca = ca
    self.antecedente = antecedente
    self.deslocamento = deslocamento
    self.itens = itens if itens is not None else []
    self.magias = magias if magias is not None else []
    self.truques = truques if truques is not None else []

  @classmethod
  def criar(cls):
    nome = input('Digite o nome: ')
    classe = input('Digite a classe: ')
    raca = input('Digite sua raça: ')
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
    ca = int(input('Digite o CA do personagem: '))
    antecedente = input('Digite seu antecedente: ')
    deslocamento = int(input('Digite o descolamento do personagem em Metros:'))
    
    itens = []
    novoItem = ""
    while novoItem != 'sair':
      novoItem = input("Digite o item do seu personagem ou 'sair' para fechar: ").lower()
      if novoItem != 'sair':
        itens.append(novoItem)

    magias = []
    novaMagia = ""
    while novaMagia != 'sair':
      novaMagia = input("Digite a magia do seu personagem ou 'sair' para fechar: ").lower()
      if novaMagia != 'sair':
        magias.append(novaMagia)

    truques = []
    novoTruque = ""
    while novoTruque != 'sair':
      novoTruque = input("Digite o truque do seu personagem ou 'sair' para fechar: ").lower()
      if novoTruque != 'sair':
        truques.append(novoTruque)   

    return cls(nome, classe, raca, nivel, pvMax, pvAtual, atributos, ca, antecedente, deslocamento, itens, magias, truques)

  def mostraPersonagem(self):
    print('\n================================')
    print('           RPG DECK             ')
    print('================================')

    print(f'\nNome: {self.nome}')
    print(f'Classe: {self.classe}')
    print(f'Raça: {self.raca}')
    print(f'Nível: {self.nivel}')
    print(f'Bonus de Proficiência: {self.bonusProf}')
    print(f'Classe de Armadura: {self.ca}')
    print(f'Antecedente: {self.antecedente}')
    print(f'Deslocamento: {self.deslocamento}')

    print(f'\nPV: {self.pvAtual}/{self.pvMax}')

    print('\n-------- ATRIBUTOS -----------\n')

    for atributos, valores in self.atributos.items():
      print(f"{atributos}: {valores}")

    print('\n-------- INVENTÁRIO -----------\n')

    for item in self.itens:
      print(f'Item: {item}')

    print('\n-------- Conjurações -----------\n')
    for magia in self.magias:
      print(f'Magia: {magia}')
    for truque in self.truques:
      print(f'Truque: {truque}')

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
      'raça': self.raca,
      'nivel': self.nivel,
      'PV Maximo': self.pvMax,
      'PV Atual': self.pvAtual,
      'atributos': self.atributos,
      'bonus proficiencia': self.bonusProf,
      'ca': self.ca,
      'antecedente': self.antecedente,
      'deslocamento': self.deslocamento,
      'itens': self.itens,
      'magias': self.magias,
      'truques': self.truques
    }

    return personagem

  @classmethod
  def de_dict(cls, dados):
    nome = dados['nome']
    classe = dados['classe']
    raca = dados['raça']
    nivel = dados['nivel']
    pvMax = dados['PV Maximo']  
    pvAtual = dados['PV Atual']
    atributos = dados['atributos']
    ca = dados['ca']
    antecedente = dados['antecedente']
    deslocamento = dados['deslocamento']
    itens = dados['itens']
    magias = dados['magias']
    truques = dados['truques']

    return cls(nome, classe, raca, nivel, pvMax, pvAtual, atributos, ca, antecedente, deslocamento, itens, magias, truques)


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