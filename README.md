# Boletim Escolar em Python

Este é um projeto simples em Python que calcula a média de um aluno com base em três notas e informa se ele foi aprovado, está em recuperação ou reprovado, considerando também a frequência.

## Objetivo

Praticar:
- Entrada de dados (`input`)
- Conversão de tipos (`float`)
- Operações matemáticas
- Estruturas condicionais (`if`, `elif`, `else`)
- Lógica de decisão em Python

## O que o programa faz

O programa:
- Pede o nome do aluno  
- Pede três notas  
- Pede a frequência (%)  
- Calcula a média das notas  
- Mostra:
  - Nome do aluno  
  - Média final (com duas casas decimais)  
  - Frequência  
  - Status final do aluno  

### Regras de aprovação
- Média *≥ 7.0* e frequência *≥ 75%* → *Aprovado*
- Média *entre 5.0 e 6.9* e frequência *≥ 75%* → *Recuperação*
- Caso contrário → *Reprovado*  

## Como executar

1. Tenha o Python instalado  
2. Baixe ou clone este repositório  
3. No terminal, execute:
```
python boletim.py
```
4. Siga as instruções na tela
#Exemplo de execução
Nome:Thiago Augusto
nota 2:7.0
nota 2:8.5
nota 3:9.0
frequência: 86
-Resultado:
média:8.17
Aprovado✓
