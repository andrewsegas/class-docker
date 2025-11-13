from flask import Flask
import os

app = Flask(__name__)

CONTADOR_PATH = "data/contador.txt"

@app.route("/")
def index():
    os.makedirs("data", exist_ok=True)
    
    if not os.path.exists(CONTADOR_PATH):
        with open(CONTADOR_PATH, "w") as f:
            f.write("0")

    with open(CONTADOR_PATH, "r+") as f:
        valor = int(f.read())
        valor += 1
        f.seek(0)
        f.write(str(valor))
        f.truncate()

    return f"A aplicação foi acessada {valor} vezes."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
