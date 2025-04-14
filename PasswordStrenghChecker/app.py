from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    feedback = []
    strength = 0

    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters).")
    else:
        strength += 1

    if not re.search(r"[a-z]", password):
        feedback.append("Add lowercase letters.")
    else:
        strength += 1

    if not re.search(r"[A-Z]", password):
        feedback.append("Add uppercase letters.")
    else:
        strength += 1

    if not re.search(r"[0-9]", password):
        feedback.append("Add numbers.")
    else:
        strength += 1

    if not re.search(r"[\W_]", password):
        feedback.append("Add special characters (!@#$ etc.).")
    else:
        strength += 1

    if strength == 5:
        status = "Strong"
    elif strength >= 3:
        status = "Medium"
    else:
        status = "Weak"

    return status, feedback

@app.route("/", methods=["GET", "POST"])
def index():
    feedback = None
    status = None
    submitted = False

    if request.method == "POST":
        submitted = True
        password = request.form.get("password", "").strip()
        if password:
            status, feedback = check_password_strength(password)

    return render_template("index.html", feedback=feedback, status=status, submitted=submitted)

if __name__ == "__main__":
    app.run(debug=True)
