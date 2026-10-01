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
    nome = input('\033[91mDigite o nome: \033[0m')
    classe = input('\033[91mDigite a classe: \033[0m')
    raca = input('\033[91mDigite sua raça: \033[0m')
    nivel = int(input('\033[91mDigite o nivel do personagem: \033[0m'))
    pvMax = int(input('\033[91mDigite o PV Máximo: \033[0m'))
    pvAtual = int(input('\033[91mDigite o PV Atual: \033[0m'))
    atributos = {
      'Força': int(input('\033[91mDigite a valor da Força do personagem: \033[0m')),
      'Destreza': int(input('\033[91mDigite a valor da Destreza do personagem: \033[0m')),
      'Constituição': int(input('\033[91mDigite a valor da Constituição do personagem: \033[0m')),
      'Inteligencia': int(input('\033[91mDigite a valor da Inteligencia do personagem: \033[0m')),
      'Sabedoria': int(input('\033[91mDigite a valor da Sabedoria do personagem: \033[0m')),
      'Carisma': int(input('\033[91mDigite a valor do Carisma do personagem: \033[0m'))
    }
    ca = int(input('\033[91mDigite o CA do personagem: \033[0m'))
    antecedente = input('\033[91mDigite seu antecedente: \033[0m')
    deslocamento = int(input('\033[91mDigite o descolamento do personagem em Metros: \033[0m'))
    
    itens = []
    novoItem = ""
    while novoItem != 'sair':
      novoItem = input("\033[91mDigite o item do seu personagem ou 'sair' para fechar: \033[0m").lower()
      if novoItem != 'sair':
        itens.append(novoItem)

    magias = []
    novaMagia = ""
    while novaMagia != 'sair':
      novaMagia = input("\033[91mDigite a magia do seu personagem ou 'sair' para fechar: \033[0m").lower()
      if novaMagia != 'sair':
        magias.append(novaMagia)

    truques = []
    novoTruque = ""
    while novoTruque != 'sair':
      novoTruque = input("\033[91mDigite o truque do seu personagem ou 'sair' para fechar: \033[0m").lower()
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

