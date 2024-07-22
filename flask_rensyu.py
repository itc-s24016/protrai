#s24016
#flaskの練習
#h1タグの大きさでHello World表示される

from flask import Flask#インストール済みのflaskモジュールのFlaskクラスをインポート

app = Flask(__name__)#appという変数にクラスをインスタンス化
#その際、コンストラクタ（特別な変数）への引数は実行中のモジュールを指定する

@app.route('/')#ルートURLに対するリクエストを処理する関数を定義するデコレーター
#引数にルート'/'を指定するとアクセスした際index()関数が呼び出される
def index():
    return "<h1>Hello World</h1>"

if __name__ == '__main__':
    app.run(debug = True)

