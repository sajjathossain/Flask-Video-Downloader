from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
import youtube_dl

ulink = ""

app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/terms-conditions")
def terms():
    return render_template("terms-conditions.html")


@app.route("/privacy-policy")
def privacy():
    return render_template("privacy-policy.html")


@app.route("/formats", methods=["GET","POST"])
def formats():
    uLink = request.form['url']
    with youtube_dl.YoutubeDL() as ydl:
        url = ydl.extract_info(uLink, download=False)
        vidFormats = url["formats"]
    return render_template("formats.html", vFormats=vidFormats, iFr=url, tLink=uLink)


@app.route("/download", methods=["GET", "POST"])
def download():
    dnLink = request.form['fUrl']
    formatsID = int(request.form["fId"])
    with youtube_dl.YoutubeDL() as ydl:
        url = ydl.extract_info(dnLink, download=False)
        downloadLink = (url["formats"][formatsID]["url"])
        
    return redirect(downloadLink+"&dl=1")
    # return render_template("download.html", vals=formatsID)


@app.route("/downloadBest", methods=["GET", "POST"])
def downloadBest():
    dnLink = request.form['fUrl']
    formatsID = int(request.form["fId"])
    with youtube_dl.YoutubeDL() as ydl:
        url = ydl.extract_info(dnLink, download=False)
        downloadLink = (url["formats"][-1]["url"])
            
        
    return redirect(downloadLink+"&dl=1")
    # return render_template("download.html", vals=formatsID)
if __name__ == "__main__":
    app.run(debug=True)