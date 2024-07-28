#s24016
#Flaskを使った簡単なメッセージアプリ
#protrai/flask_msg_rensyu.py
#実行はgit bashでpython flask_msg_rensyu.py（バックエンド側にあたる）
#フロントエンド部分のHTMLをtemplates/msg.html
#実際のメッセージを記録するファイルはprotrai/data.txtとする

from flask import Flask, render_template, request
import datetime

app = Flask(__name__)#インスタンス化

@app.route("/")#こんにちは世界
def index():
    return render_template("index.html")

@app.route("/himitsu")#秘密のページへ
def himitsy():
    return "<small>秘密のページ</small>"

@app.route("/msg")#メッセージ入力フォームへ
def msg():
    return render_template("msg.html")

@app.route("/submit", methods=["POST"])
def submit():
    content = request.form["content"]#入力された内容を取得
    with open("data.txt", "a") as file:#data.txtに追記する
        file.write(f"\n{datetime.datetime.now()}\n{content}\n")
        return f"書き込みました"

    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "5000", debug = True)
