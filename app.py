from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "top job. nice work\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
