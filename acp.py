from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    bmi = ""

    if request.method == "POST":
        weight = float(request.form.get("Weight"))
        height = float(request.form.get("Height"))

        bmi = round(weight / ((height / 100) ** 2), 2)

    return render_template("index1.html", bmi=bmi)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)