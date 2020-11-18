from flask import Flask
from wsgiref.simple_server import make_server
app = Flask(__name__)

@app.route('/api/v1/hello-world-30')
def show_student_id():
    # show the user profile for that user
    return 'Hello World 30 '

with make_server('',5000,app) as server:
    print('http://127.0.0.1:5000/api/v1/hello-world-30')

    server.serve_forever()

#if __name__ == "__main__":
#    app.run()