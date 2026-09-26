from flask import Flask, request, render_template, session, redirect, url_for  
import database 

app = Flask(__name__)
app.config["SECRET_KEY"] = "Mbledos"

@app.route("/")
def index():
    quizzes = database.get_quizzes()
    return render_template("index.html", quizzes=quizzes)   

@app.route("/start", methods=["POST"])
def start():
    quiz_id = int(request.form.get("quiz_id"))
    rows = database.get_questions(quiz_id)
    questions = [{"q": r[0], "a": r[1], "w": [r[2], r[3], r[4]]} for r in rows]
    session["questions"] = questions
    session["nomor"] = 0
    session["skor"] = 0
    return redirect(url_for("test"))

if __name__ == "__main__":
    app.run(debug=True)