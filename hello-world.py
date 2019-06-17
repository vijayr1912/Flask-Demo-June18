from flask import Flask

app = Flask(__name__)

@app.route("/")
def samta():
    return "SIH cross skilling session on Python Flask!"

if __name__ == '__main__':
    print('Welocme to Python Flask programming')
    print(app)
    app.run(port=5000, debug=True)
