import random

def coll_word():
    list_w = ['cat', 'push', 'pen', 'our', 'liz', 'wood']
    return list_w[random.randint(0,len(list_w))]

def hangman():
    word = coll_word()
    wrong = -1
    stages = ['________        ',
              '|       |       ',
              '|       |       ',
              '|       O       ',
              '|      /|\      ',
              '|      / \      ',
              '[]   hangman    ']
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('ハングマンへようこそ！')
    while wrong < len(stages) - 1:
        print('\n')
        msg = '1文字を予測してね: '
        char = input(msg)
        if char in rletters:
            print('1文字当たり！')
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            print('はずれ～')
            wrong += 1
        print('\"' + ' '.join(board) + '\"')
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('\nあなたの勝ち！')
            print('\"' + ' '.join(board) + '\"')
            win = True
            break
    if not win:
        print('\nあなたの負け！正解は\"{}\"'.format(word))
#        print('\n'.join(stages[0:wrong+1]))

#hangman('cat')
hangman()
