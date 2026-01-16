# CRIAÇÃO DE BOLETIM ESCOLAR
# 
nome = input("Digite o nome completo do aluno: ")

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

frequencia = float(input("Digite a frequência do aluno (%): "))

# Cálculo da média
media = (nota_1 + nota_2 + nota_3) / 3

# Exibição dos resultados
print(f"\nAluno: {nome}")
print(f"Média final: {media:.2f}")
print(f"Frequência: {frequencia}%")

# Decisão do status
if media >= 7 and frequencia >= 75:
    print("Status: APROVADO")
elif media >= 5 and frequencia >= 75:
    print("Status: RECUPERAÇÃO")
else:
    print("Status: REPROVADO")
