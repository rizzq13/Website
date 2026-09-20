import sqlite3

DB = "quiz.db"   # database yang sama, dipakai terus sampai Lesson 8


def buat_tabel():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    # Tabel 1: daftar quiz
    c.execute("""CREATE TABLE IF NOT EXISTS quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT
    )""")

    # Tabel 2: soal. quiz_id = soal ini milik quiz yang mana.
    c.execute("""CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quiz_id INTEGER,
        question TEXT,
        correct TEXT,
        wrong1 TEXT,
        wrong2 TEXT,
        wrong3 TEXT
    )""")

    conn.commit()
    conn.close()
    print("[OK] 2 tabel siap: quizzes + questions.")


def isi_data():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    # Cek dulu: kalau sudah ada isinya, jangan diisi lagi (biar tidak dobel).
    c.execute("SELECT COUNT(*) FROM quizzes")
    if c.fetchone()[0] > 0:
        print("[i] Data sudah ada, tidak diisi ulang.")
        conn.close()
        return

    # Quiz 1: Python
    c.execute("INSERT INTO quizzes (name, description) VALUES (?, ?)",
              ("Python Basics", "Soal dasar pemrograman Python"))
    pid = c.lastrowid   # id quiz yang baru dibuat
    c.executemany(
        "INSERT INTO questions (quiz_id, question, correct, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?,?)",
        [
            (pid, "print(2**3) hasilnya?", "8", "6", "9", "12"),
            (pid, "Tipe data True adalah?", "bool", "int", "str", "list"),
            (pid, "Fungsi untuk input user?", "input()", "print()", "len()", "range()"),
            (pid, "Simbol komentar di Python?", "#", "//", "<!--", "/*"),
            (pid, "List itu?", "Koleksi data", "Tipe angka", "Fungsi", "String"),
        ])

    # Quiz 2: Web
    c.execute("INSERT INTO quizzes (name, description) VALUES (?, ?)",
              ("Web Dasar", "Soal HTML, CSS, dan Flask"))
    wid = c.lastrowid
    c.executemany(
        "INSERT INTO questions (quiz_id, question, correct, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?,?)",
        [
            (wid, "HTML singkatan dari?", "HyperText Markup Language", "High Tech Modern", "Home Tool ML", "Hyper Transfer ML"),
            (wid, "CSS untuk apa?", "Styling halaman", "Database", "Server", "Security"),
            (wid, "Tag paragraf di HTML?", "<p>", "<h1>", "<div>", "<br>"),
            (wid, "Flask adalah?", "Web framework Python", "Database", "Game engine", "Text editor"),
            (wid, "SQL singkatan dari?", "Structured Query Language", "Simple Query", "System Query", "Server Query"),
        ])

    conn.commit()
    conn.close()
    print("[OK] 2 quiz + 10 soal dimasukkan.")


def get_quizzes():
    """Ambil daftar quiz. Dipakai halaman depan (Lesson 5-8)."""
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT id, name, description FROM quizzes")
    hasil = c.fetchall()
    conn.close()
    return hasil


def get_questions(quiz_id):
    """Ambil semua soal milik satu quiz. Dipakai halaman /quiz dan /test."""
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT question, correct, wrong1, wrong2, wrong3 FROM questions WHERE quiz_id = ?", (quiz_id,))
    hasil = c.fetchall()
    conn.close()
    return hasil


def tampil_join():
    """JOIN: gabung tabel questions + quizzes biar tahu nama quiz tiap soal."""
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""SELECT quizzes.name, questions.question
                 FROM questions
                 JOIN quizzes ON questions.quiz_id = quizzes.id""")
    print("\n--- Semua soal + nama quiz (JOIN) ---")
    for row in c.fetchall():
        print(f"  [{row[0]}] {row[1]}")
    conn.close()


if __name__ == "__main__":
    buat_tabel()
    isi_data()
    tampil_join()
