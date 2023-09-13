# Jogo da velha em Python com inteligencia artificial usando o algoritmo Minimax.
# By Sammuel Gusmão Martins
# Programa Criado durante a disciplina de Inteligencia Artificial do curso de Sistemas de Informação da UNEX Vitória da Conquista - BA
import random
import sys

# Cria um tabuleiro
tabuleiro = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]

# Método para exibir o tabuleiro
def exibir_tabuleiro():
    for i in tabuleiro:  # Percorre o tabuleiro
        print("|".join(i))  # Imprime o tabuleiro

# Movimentos do Jogador Humano:
# Permita que o jogador humano faça movimentos digitando as coordenadas da posição onde deseja jogar. 
# Você deve validar se a posição está vazia e se as coordenadas são válidas.
def jogada_humana():
    print("Sua vez de jogar!\n Digite a posição que deseja jogar: ")
    jogada = int(input()) # Recebe a posição que o jogador deseja jogar
    if tabuleiro[jogada // 3][jogada % 3] == chr(jogada + 1) : # Verifica se a posição está vaga através da conversão do número para o caractere correspondente dentro do tabuleiro
        # Divide por 3 para obter o cociente (a linha) e pega o resto da divisão por 3 para obter a coluna Ex.: 5 / 3 = 1 (Cociente) e 5 % 3 = 2 (Resto)
        tabuleiro[jogada // 3][jogada % 3] = "X" # Marca a posição com o caractere X, se a posição estiver vaga
        exibir_tabuleiro()        

exibir_tabuleiro() # Exibe o tabuleiro
jogada_humana()

def jogada_ia():
    print("Vez da IA jogar...")
    # Implemente aqui a lógica Minimax com Alpha-Beta Pruning para determinar a melhor jogada da IA
    # Depois, atualize o tabuleiro com a jogada escolhida pela IA e exiba o tabuleiro
    exibir_tabuleiro()
