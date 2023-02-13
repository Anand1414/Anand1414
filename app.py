from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print('Good morning')

if __name__ == '__main__':
    print('yes')