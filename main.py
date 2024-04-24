print('-------------------------------')
print('Financeiro 1b 1/2 ver. 1.0.5')

listaClParc = []
listaVlrParc = []

while True:

  print('-------------------------------')
  print('Para Adicionar parcela, digite 1')
  print('Para Visualizar parcelas, digite 2')
  print('Para Baixa de parcelas, digite 3')
  print('Ou, para fechar, digite 0')
  mod1 = input('Selecione o serviço desejado: ')
  
  if mod1 == '1':
    print('-----------------------')
    print('Adicionar parcela')
    print('-----------------------')
    parcelaAddCl = input('Para qual cliente deseja adicionar a parcela? ')
    print('Cliente', parcelaAddCl, 'selecionado')
    print('Qual valor deve ser adicionado? ')
    parcelaAddVlr = (input('R$' ))
    nrParcela =+ 1
    listaClParc.append(parcelaAddCl)
    listaVlrParc.append(parcelaAddVlr)
    print('Ok, uma parcela de R$', parcelaAddVlr,'foi adicionada ao cliente', parcelaAddCl, 'como parcela', nrParcela)
  
  elif mod1 == '2':
    print('-----------------------')
    print('Visualizar parcelas')
    print('-----------------------')
    for parcelas in listaVlrParc:
        print('Cliente', listaClParc)
        print('Valor', listaVlrParc)
        break

  elif mod1 == '3':
    print('-----------------------')
    print('Baixa de parcelas')
    print('-----------------------')

    print('A ultima parcela será deletada, tem certeza?')
    parcelaDelCl = input('Digite "Sim" ou "Não" ')
    if parcelaDelCl == 'Sim':
      del listaClParc[0]
      del listaVlrParc [0]
      print('Ok, a última parcela da lista foi deletada')
    elif parcelaDelCl == 'sim':
      del listaClParc[0]
      del listaVlrParc [0]
      print('Ok, a última parcela da lista foi deletada')
    elif parcelaDelCl == 'SIM':
      del listaClParc[0]
      del listaVlrParc [0]
      print('Ok, a última parcela da lista foi deletada')
    elif parcelaDelCl == 'Não':
      continue
    elif parcelaDelCl == 'nao':
      continue
    elif parcelaDelCl == 'não':
      continue
    elif parcelaDelCl == 'Nao':
      continue
    elif parcelaDelCl == 'NÃO':
      continue
    elif parcelaDelCl == 'NAO':
      continue
    else:
        print('Erro ao processar confirmação, tente novamente mais tarde.')
 
  elif mod1 == '0':
    break

  else:
    print('-----------------------')
    print('Não entendi, escolha uma das opções:')
    continue
