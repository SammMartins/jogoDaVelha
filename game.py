class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    def exibir_tabuleiro(self):
        for row in self.tabuleiro:
            print("|".join(row))

    def verificar_vitoria(self, jogador):
        # Verificar linhas, colunas e diagonais
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] == jogador:
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] == jogador:
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == jogador:
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == jogador:
            return True
        return False

    def verificar_empate(self):
        for row in self.tabuleiro:
            for posicao in row:
                if posicao == " ":
                    return False
        return True

    def fazer_jogada(self, jogador, linha, coluna):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = jogador
            return True
        else:
            return False


class Jogador:
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def fazer_jogada(self, tabuleiro):
        pass


class JogadorHumano(Jogador):
    def fazer_jogada(self, tabuleiro):
        while True:
            try:
                print("Sua vez de jogar!\nDigite a linha e a coluna separadas por espaço (ex: 1 2): ")
                linha, coluna = map(int, input().split())
                linha -= 1
                coluna -= 1

                if 0 <= linha < 3 and 0 <= coluna < 3:
                    if tabuleiro.fazer_jogada(self.simbolo, linha, coluna):
                        break
                    else:
                        print("Posição ocupada! Tente novamente.")
                else:
                    print("Posição inválida! As posições válidas são de 1 a 3 para linha e coluna.")
            except ValueError:
                print("Entrada inválida. Digite linha e coluna separadas por espaço (ex: 1 2).")


class IA(Jogador):
    def fazer_jogada(self, tabuleiro):
        _, melhor_jogada = self.minimax(tabuleiro, self.simbolo)
        tabuleiro.fazer_jogada(self.simbolo, melhor_jogada[0], melhor_jogada[1])

    def minimax(self, tabuleiro, jogador):
        if tabuleiro.verificar_vitoria(self.simbolo):
            return 1, None
        elif tabuleiro.verificar_vitoria("X" if self.simbolo == "O" else "O"):
            return -1, None
        elif tabuleiro.verificar_empate():
            return 0, None

        if jogador == self.simbolo:
            melhor_pontuacao = -float("inf")
            melhor_jogada = None
            for i in range(3):
                for j in range(3):
                    if tabuleiro.tabuleiro[i][j] == " ":
                        tabuleiro.tabuleiro[i][j] = jogador
                        pontuacao, _ = self.minimax(tabuleiro, "X" if jogador == "O" else "O")
                        tabuleiro.tabuleiro[i][j] = " "
                        if pontuacao > melhor_pontuacao:
                            melhor_pontuacao = pontuacao
                            melhor_jogada = (i, j)
            return melhor_pontuacao, melhor_jogada
        else:
            melhor_pontuacao = float("inf")
            melhor_jogada = None
            for i in range(3):
                for j in range(3):
                    if tabuleiro.tabuleiro[i][j] == " ":
                        tabuleiro.tabuleiro[i][j] = jogador
                        pontuacao, _ = self.minimax(tabuleiro, "X" if jogador == "O" else "O")
                        tabuleiro.tabuleiro[i][j] = " "
                        if pontuacao < melhor_pontuacao:
                            melhor_pontuacao = pontuacao
                            melhor_jogada = (i, j)
            return melhor_pontuacao, melhor_jogada


def main():
    tabuleiro = Tabuleiro()
    jogador_humano = JogadorHumano("X")
    ia = IA("O")
    jogador_atual = jogador_humano

    while not (tabuleiro.verificar_vitoria(jogador_humano.simbolo) or tabuleiro.verificar_vitoria(ia.simbolo) or tabuleiro.verificar_empate()):
        tabuleiro.exibir_tabuleiro()
        jogador_atual.fazer_jogada(tabuleiro)
        jogador_atual = ia if jogador_atual == jogador_humano else jogador_humano

    tabuleiro.exibir_tabuleiro()
    if tabuleiro.verificar_vitoria(jogador_humano.simbolo):
        print("Você venceu!")
    elif tabuleiro.verificar_vitoria(ia.simbolo):
        print("A IA venceu!")
    else:
        print("Empate!")


if __name__ == "__main__":
    main()
