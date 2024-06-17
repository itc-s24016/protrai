#s24016
#def4アレンジ　メインの処理をmain()関数に行わせるプログラム
import random
def omikuji():
    kuji=["大吉","中吉","小吉","凶"]
    return random.choice(kuji)

kekka=omikuji()


def main():
    print("結果は",kekka,"です")

main()
