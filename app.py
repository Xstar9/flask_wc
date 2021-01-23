#   快捷键    ctrl+R 替换   ctrl+F（搜索）

from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def Home():
    return index()

@app.route('/movie')
def movie():
    datalist = []
    conn = sqlite3.connect("Doubanmovies.db")
    cur = conn.cursor()
    sql = "select * from DouBanMovie"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template("movie.html",moives = datalist)

@app.route('/score')
def score():
    score =[] #评分
    num =[] # 该评分电影数量
    conn = sqlite3.connect("Doubanmovies.db")
    cur = conn.cursor()
    sql = "select score, count(score) from DouBanMovie group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    conn.close()
    return render_template("score.html",score=score, num=num)

@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")

if __name__ == '__main__':
    app.run()
