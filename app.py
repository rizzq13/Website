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

@app.route("/test", methods=["GET", "POST"])
def test():
    soal = database.get_questions(session["quiz_id"])
    nomor = session["nomor"]

    if request.method == "POST":
        jawaban = request.form.get("jawaban")
        benar = soal[nomor][1]
        if jawaban == benar:
            session["skor"] = session["skor"] + 1
        session["nomor"] = nomor + 1
        nomor = session["nomor"]

    if nomor >= len(soal):
        return redirect(url_for("result"))

    baris = soal[nomor]
    pertanyaan = baris[0]
    pilihan = [baris[1], baris[2], baris[3], baris[4]]

    return render_template("test.html", pertanyaan=pertanyaan, pilihan=pilihan, nomor=nomor + 1, total=len(soal), skor=session["skor"])

@app.route ("/result")
def result():
    skor = session["skor"]
    total = len(database.get_questions(session["quiz_id"]))
    return render_template("result.html", skor=skor, total=total)



if __name__ == "__main__":
    app.run(debug=True)