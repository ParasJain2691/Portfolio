from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html')


@app.route("/experience")
def experience():
  return render_template("experience.html")


@app.route("/education")
def education():
  return render_template("education.html")


@app.route("/certificates")
def certificates():
  return render_template("certificates.html")


@app.route("/skills")
def skills():
  return render_template("skills.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
