#s24016
#flask_rensyuのver.2
#「こんにちは世界」と書かれたhtml文章を表示するプログラム

from flask import Flask, render_template#render_templateはhtmlを扱う際に必要なモジュール

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")#templates/index.htmlを事前に作成しておく

if __name__ == '__main__':#それぞれのIPアドレスでアクセスするように設定
    app.run(host = "0.0.0.0", port = 5000, debug = True)

#python flask_rensyu2.pyで実行し、ブラウザから表示させてみる
