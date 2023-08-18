from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Cia mano pirmasis home puslapis su Flask</h1>"
@app.route("/<kintamasis>")
def user(kintamasis):
    return f"Sveiki {kintamasis} atvykes i Flask page'a"




if __name__ == "__main__":
    app.run()
