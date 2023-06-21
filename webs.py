from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	l = "React"
	return render_template("index.html",lang=l)

if __name__=='__main__':
	app.run()

