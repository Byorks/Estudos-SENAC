print("Olá, Mundo!")

# Vizualizando todas as palavras reservadas
import keyword

print(keyword.kwlist, "\n")

# Função print e seus parâmetros
# sep -> define o separador entre os valores inserídosm
# end -> define o caractere de finalização de linha
# file -> especifica onde a saida será enviada, por padrão para o terminal
# flush -> se True, força a saída imediata(útil para logs em tempo real)
#print(valor1, valor2, ..., valorN, sep=' ', end='\n', file=sys.stdout, flush=False)

# Alterando o separado padrão do print
print('Python', 'é', 'incrível!', sep='-' ) # Python-é-incrível!

# Alterando comportamento final do print
print('Linha 1', end=' ')
print('Linha 2') # Linha 1 Linha 2

# Utilizando f-strings
nome = 'Ana'
idade = 25
print(f'Meu nome é {nome} e eu tenho {idade} anos.')

numero = 7
print(f'O dobro de {numero} é {numero * 2}.')

print("Eu sou o snoopynhu!")

# Formatando string a partir de número decimal
numero = 1.323542

print("Valor formatado com duas casas decimais: {:.2f}".format(numero))

# com f-string
print(f"Valor formatado com f-string: {numero:.2f}")

# Entrada de dados do usuário
variavel = input("Aqui fica a mensagem do pedido: ")

print("Você digitou:", variavel)

# Conversão para int e float
idade = int(input("Digite a sua idade: "))

print(f"Você tem {idade} anos.")

salario = float(input("Digite o seu salário: "))
print(f"Seu salário é R$ {salario:.2f}.")