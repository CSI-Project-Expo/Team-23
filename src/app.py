from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":
            return "Access Granted 🎉"
        else:
            return "Invalid Credentials ❌"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

