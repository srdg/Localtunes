from flask import Flask,request,render_template
import os

app = Flask(__name__)

# route to the homepage
@app.route('/')
def index(url_music=None):
	url_music = os.listdir(os.getcwd()+'/static/music')
	url_music = ['music/'+i for i in url_music]
	print(url_music)
	return render_template("index.html",url_music=url_music)

if __name__=="__main__":
	app.run(debug=True)