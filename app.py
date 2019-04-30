from flask import Flask

app = Flask(__name__)


# @app.route('/')
# def user_page():
#     return '<h1>Hello Totoro!</h1><img src = "http://helloflask.com/totoro.gif">'

@app.route('/')
def cc():
    page =open ('cc.html',encoding='utf-8')
    res = page.read()
    # page.clos()
    return res


if __name__ == '__main__':
    app.run(Debug=True)
