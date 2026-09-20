from flask import Flask, request

app = Flask(__name__)
@app.route('/sapa')
def sapa():
    nama = request.args.get('nama', 'Tamu')
    return """ 
        <h1>Halo, """ + nama + """!</h1>
        <form method="GET">
           <input name="nama" placeholder="Masukkan nama Anda" >
           <button type="submit">sapa</button>
           </form>
           <a href="/">Kembali ke Halaman Utama</a>
           """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "admin123":
            return "<h1>Login Berhasil!</h1><p>Selamat datang, admin!</p>"
        else:
            return "<h1>Login Gagal!</h1><p>Username atau password salah.</p>"
    return """
        <h1>Login</h1>88
        <form method="POST">
            <input name="username" placeholder="Username" required>
            <input name="password" type="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        <a href="/">Kembali ke Halaman Utama</a>
    """
app.run(debug=True)