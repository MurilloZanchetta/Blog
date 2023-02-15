from flask import Flask, render_template, Request, request
app = Flask(__name__)

comentarios = []


@app.route("/", methods=["GET", "POST"])
def index():
    comentario = request.form.get("comentar")
    comentarios.append(comentario)
    return render_template("index.html", comentarios=comentarios)

if __name__ == "__main__":
        app.run(debug=True)
