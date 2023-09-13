import random
import sys


# Cria um tabuleiro
tabuleiro = [['   ' for _ in range(3)] for _ in range(3)]
# Método para exibir o tabuleiro
def exibir_tabuleiro():
    count = 0
    for linha in tabuleiro:
        count+= 1
        print('|'.join(linha))
        if(count == 3):
          break
        print('---' * 4)

exibir_tabuleiro()