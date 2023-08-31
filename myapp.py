from flask import Flask, render_template

app = Flask(__name__)


users_database = {
    "Mjnorvor": "1100",
    "User1" : "password"
    }

@app.route('/')
def login():
    return render_template('login.html')

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)