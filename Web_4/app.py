from flask import *
import mlab
from youtube_dl import YoutubeDL
from models.video import Video

app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/admin", methods =["GET", "POST"])
def admin():
    if request.method == "GET":
        videos = Video.objects()
        return render_template("admin.html", videos = videos)
    elif request.method == "POST":
        form = request.form
        link = form["link"]
        ydl = YoutubeDL()
        data = ydl.extract_info(link, download = False)
        title = data["title"]
        thumbnail = data["thumbnail"]
        views = data["view_count"]
        youtube_id = data["id"]

        new_video = Video(title = title,    
                          thumbnail = thumbnail,
                          views = views,
                          link = link,
                          youtube_id = youtube_id
        )
        new_video.save()

        return "saved"

if __name__ == '__main__':
  app.run(debug=True)

