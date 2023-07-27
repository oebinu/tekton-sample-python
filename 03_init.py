from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def web():
   return "OEBINU's flask web page"

@app.route('/dog')
def image():
   return render_template("03_index.html")

if __name__ == "__main__":
   app.run(host="0.0.0.0")