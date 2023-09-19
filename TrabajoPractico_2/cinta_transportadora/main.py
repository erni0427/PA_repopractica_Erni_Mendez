# Aplicación principal
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method =="POST":     
        n=request.form["n"]
        return render_template("menú.html", )
    else:
        return render_template("menú.html", aw_F= "", aw_V="", aw_m="", aw_k="", aw_p="", aw_z="", aw_T="")

if __name__ == "__main__":
  app.run(debug=True)