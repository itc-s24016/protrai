#s24016
#himitsuのページを開く
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    return "test"

@app.route('/himitsu')
def himitsu():
    return"""
<h1>秘密のページ</h1>
<button onclick="location.href='/'">ホームに戻る</button>
"""

if __name__ == '__main__':#それぞれのIPアドレスでアクセスするように設定
    app.run(host = "0.0.0.0", port = 5000, debug = True)
