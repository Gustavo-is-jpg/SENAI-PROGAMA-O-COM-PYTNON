nome =  'Gustavo'
sobrenome = 'Gomes'
print(nome, sobrenome)

print(f'Meu nome completo é {nome} {sobrenome}')


escola = 'SENAI Mairinque'
print(escola[0:6])


escola = 'SENAI Mairinque - PS'

posicao = escola.find('Mairinque')
print(posicao)

print('Substituindo de texto', escola.replace('Mairinque', 'aluminio'))

verdadeiro = True

#print(verdadeiro)

falso = False
#print(falso)

saldo_conta = 200
valor_do_saque = 100
pode_executar_saque =  valor_do_saque <=  saldo_conta

print(pode_executar_saque)