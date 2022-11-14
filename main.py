from random import randint, sample


def chooseWord():
    wordsList = ["Kiwi", "Maçã", "Banana", "Melancia", "Pêssego", "Uva", "Manga", "Pera", "Abacate", "Abacaxi"]
    random = randint(0, (len(wordsList) - 1))
    word = wordsList[random]
    return word


def wordShuffle(word):
    shuffled = ''.join(sample(word, len(word)))
    return shuffled


def guessWord(wordSuffled, word):
    w = f'A palavra embaralhada era: {word.title()}'
    i = 6
    while i > 0:
        print(f'A palavra embaralhada é: -> {wordSuffled} <-')
        answer = str(input('    Digite qual é a palavra: ')).lower()
        print()
        if answer == word.lower():
            print('[ACERTOU!]')
            break
        else:
            print('[ERRADO!]')
            print(f'Você tem {i - 1} tentativas restantes.\n')
        i -= 1
    print('=' * 50)
    print(w)
    print('=' * 50)


def playAgain():
    while True:
        answer = str(input('Deseja jogar novamente (S/N): ')).upper()
        if answer == 'S':
            print()
            primary()
        elif answer == 'N':
            print('Ok... Encerrando o jogo!')
            break
        else:
            print('[RESPOSTA INVÁLIDA]')


def primary():
    print('=' * 20, 'O TEMA DAS PALAVRAS É FRUTAS', '=' * 20)
    word = chooseWord()
    shuffled = wordShuffle(word)
    guessWord(shuffled, word)
    playAgain()


if __name__ == '__main__':
    primary()
