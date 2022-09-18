from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Arambiklamaaama"

if __name__ == "__main__":
  app.run()