from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1><p>Ini adalah halaman utama dari aplikasi Flask.</p>'

@app.route('/test')
def test():
    return""""
    <h1>Soal 1</h1>
    <p>1+1 = ?</p>
    <a href="/result">Lihat Hasil</a>
    """

@app.route('/result')
def result():
    return"""
    <h1>Skor: 100/100%</h1>
    <p>Bolehh</p>
    <a href="/test">Balik ke Soal</a>
    """

app.run(debug=True)