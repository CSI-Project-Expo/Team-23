from flask import Flask, render_template, request, session, redirect, url_for
from store_data import store_pattern
from compare import compare_pattern
import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"  # needed for session

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        pattern_data = request.form.get("pattern")

        if pattern_data:
            new_pattern = list(map(float, pattern_data.split(",")))
        else:
            new_pattern = []

        if username == "admin" and password == "1234":
            suspicious = compare_pattern(username, new_pattern)
            store_pattern(username, new_pattern)

            avg_speed = round(sum(new_pattern)/len(new_pattern), 3) if new_pattern else 0
            match_score = max(10, 100 - int(avg_speed * 100))

            if suspicious:
                status = "⚠ Suspicious Login Detected"
                status_color = "red"
                risk_level = "High"
            else:
                status = "✅ Behavior Verified"
                status_color = "green"
                risk_level = "Low"

            login_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            # Save info in session
            session["username"] = username
            session["pattern"] = new_pattern
            session["avg_speed"] = avg_speed
            session["match_score"] = match_score
            session["risk_level"] = risk_level
            session["status"] = status
            session["status_color"] = status_color
            session["login_time"] = login_time

            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Invalid Credentials ❌")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session.get("username"),
        pattern=session.get("pattern"),
        avg_speed=session.get("avg_speed"),
        match_score=session.get("match_score"),
        risk_level=session.get("risk_level"),
        status=session.get("status"),
        status_color=session.get("status_color"),
        login_time=session.get("login_time")
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
