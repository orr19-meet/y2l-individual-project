from flask import Flask
app = Flask(__name__)

@app.route('/')
def add_event():
    return 'Hello, World test!'

if __name__ == '__main__':
    app.run(debug=True)

