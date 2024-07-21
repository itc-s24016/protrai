#s24016
#himitsu.py

from flask import Flask, render_template#render_templateはhtmlを扱う際に必要なモジュール

app = Flask(__name__)

@app.route('/')
def index():
    return render_templates("index.html")#templates/index.htmlを事前に作成しておく


@app.route('/himitsu')
def index_himitsu():
    return render_templates("himitsu.html")

if __name__ == '__main__':#それぞれのIPアドレスでアクセスするように設定
    app.run(host = "0.0.0.0", port = 5000, debug = True)


#python flask_rensyu2.pyで実行し、ブラウザから表示させてみる
