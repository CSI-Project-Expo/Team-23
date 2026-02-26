
from flask import Flask, render_template, request, redirect, url_for
from store_data import store_pattern
from compare_behavior import compare_pattern

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Dummy typing pattern for demo (later replace with keystroke module)
        new_pattern = [0.21, 0.19, 0.32, 0.28]

        if username == "admin" and password == "1234":

            suspicious = compare_pattern(username, new_pattern)

            if suspicious:
                return "⚠ Suspicious behaviour detected"

            store_pattern(username, new_pattern)
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Invalid Credentials ❌")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)


