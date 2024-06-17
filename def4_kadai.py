#s24016
#def4アレンジ　メインの処理をmain()関数に行わせるプログラム
import random

def omikuji():                                  #ランダムにkujiの中の一つを返す関数
    kuji=["大吉","中吉","小吉","凶"]
    return random.choice(kuji)

def main():                                      #エントリーポイントの定義
    kekka=omikuji()
    print("結果は",kekka,"です")

if __name__=="__main__":                  #if文の通りならmain関数を実行=omikuji関数が実行される
    main()
