# Jogo da velha em Python com inteligencia artificial usando o algoritmo Minimax e Orientação a objeto.
# By Sammuel Gusmão Martins
# Programa Criado durante a disciplina de Inteligencia Artificial do curso de Sistemas de Informação da UNEX Vitória da Conquista - BA
import random
import sys

# Cria um tabuleiro 3x3 com os números de 1 a 9 em cada posição
class Tabuleiro:
    def __init__(self): # __init__ é um método especial em Python que é o "construtor" da classe em Python.
        self.tabuleiro = [["1", "2", "3"], # self é uma referência ao objeto atual. É usado para acessar variáveis ​​que pertencem à classe.
                          ["4", "5", "6"],
                          ["7", "8", "9"]]

    def exibir_tabuleiro(self): # Método recebe o self como parâmetro para acessar o atributo tabuleiro da classe
        for row in self.tabuleiro:
            print("|".join(row))


class Jogador:
    def fazer_jogada(self, tabuleiro):
        pass

class JogadorHumano(Jogador): # Herda da classe Jogador
    # Movimentos do Jogador Humano:
    def fazer_jogada(self, tabuleiro):
        while True:
            try:
                print("Sua vez de jogar!\n Digite a posição que deseja jogar: ")
                jogada = int(input())  # Recebe a posição que o jogador deseja jogar
                if jogada < 1 or jogada > 9:
                    print("Posição inválida!")
                    continue # Volta para o início do loop
                # Verifica se a posição está vaga através da conversão do número para o caractere correspondente dentro do tabuleiro
                if tabuleiro[jogada // 3][jogada % 3] == chr(jogada + 1):
                    # Divide por 3 para obter o cociente (a linha) e pega o resto da divisão por 3 para obter a coluna Ex.: 5 / 3 = 1 (Cociente) e 5 % 3 = 2 (Resto)
                    # Marca a posição com o caractere X, se a posição estiver vaga
                    tabuleiro[jogada // 3][jogada % 3] = "X"
                    break # Sai do loop
                else:
                    print("Posição ocupada!")
                    continue # Volta para o início do loop
            except ValueError:
                print("Entrada inválida. Digite um número de 1 a 9.")
                continue

class IA(Jogador):
    def fazer_jogada(self, tabuleiro):
        # Lógica para a IA escolher a melhor jogada

tabuleiroMain = Tabuleiro() # Cria um objeto da classe Tabuleiro
tabuleiroMain.exibir_tabuleiro() # Chama o método exibir_tabuleiro do objeto tabuleiro