# Operadores aritméticos em Python

#  Escreva um programa em Python que receba do usuário um valor inteiro representando uma quantidade de minutos. O programa deve converter esse valor em horas e minutos, exibindo-os separadamente. Por exemplo, caso o usuário informe 135 minutos, seu programa deverá exibir como resultado 2 horas e 15 minutos.

minutos_decorridos = int(input("Digite os minutos decorridos na atividade: "))

horas = minutos_decorridos // 60
minutos = minutos_decorridos %  60

print(f"{horas} horas e {minutos} minutos")

# Importando funções Math
import math 

