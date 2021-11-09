print('{:=^40}'.format(' VAREJO SA'))
preco = float(input('Olá! Poderia informar qual o valor de sua compra? R$'))
print('')
print('''Poderia também me informar qual será a forma de pagamento? 
[ 1 ] Para à vista no dinheiro/cheque
[ 2 ] Para à vista no cartão 
[ 3 ] Para em 2x no cartão 
[ 4 ] Para 3x ou mais no cartão ''')
print(' ')
opcao = int(input('Qual será a forma de pagamento? '))
if opcao == 1:
    avista = preco - preco * (10/100)
    print('Na opção de à vista, você tem direito a 10% de desconto')
    print('Portanto, na compra no valor de {}, o valor final será de {}'.format(preco, avista))
elif opcao == 2:
    avcard = preco - preco * (5/100)
    print('Na opção de à vista no cartão, você tem direito a 5% de desconto')
    print('Portanto, na compra do valor de {}, o valor final será de {}'.format(preco, avcard))
elif opcao == 3:
    parc2 = preco/2
    print('Na opção de 2x no cartão, o valor de {} é o mesmo sem juros.'.format(preco))
    print('Portanto, a parcela sairá à {}'.format(parc2))
elif opcao == 4:
    nparc = int(input('Em quantas vezes você deseja parcelar a compra? '))
    if nparc < 3:
        print('Por favor, reinicie o programa para selecionar a opção [ 2 ]')
    else:
        precoparcela = preco / nparc
        parc3 = precoparcela + precoparcela * (20/100)
        print('Na opção de 3 ou mais parcelas, o total de parcelas escolhidas foram {}'.format(nparc))
        print('Portanto, com juros de 20%, a parcela sairá à {}'.format(parc3))
else:
    print('Opção inválida, por favor reinicie o programa.')
