

from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/about-me')
def index():
    string_1 ="""
    Name: Dao Hoang Nam
    **
    Work: PwC Vietnam
    **
    Hobbies: Games, music, books, films, finance
    **
    Favourite football club: Manchester City
    """
    return string_1

@app.route('/school')
def redirect_to_url():
    return redirect("http://techkids.vn")

if __name__ == '__main__':
  app.run(debug=True)
 