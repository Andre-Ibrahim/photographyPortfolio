from flask import Flask, render_template, url_for

app = Flask(__name__)


# instead of rewriting the card html/boostrap layout for each card 
# theres  a loop (Jinja2) that iterates over this list and palces the directory in the src
albumImg = ["../static/Pictures/_DSC1002_edited-2.jpg","../static/Pictures/_DSC0900_edited-2.jpg" , '../static/Pictures/IMG_20190602_150420955.jpg',"../static/Pictures/IMG_1191.JPG",
    "../static/Pictures/IMG_1190.JPG" ,"../static/Pictures/DSC_0930.jpg", "../static/Pictures/IMG_20190704_211825393.jpg" ]
portrait = ["DSC_0930.jpg", "DSC_0685(2).jpg" , "DSC_0665.jpg" , "DSC_0019.jpg", "DSC_0572.jpg", "DSC_0535.jpg" ,"DSC_0622.jpg", "DSC_0041.jpg", "1.jpg"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html", page="about")

@app.route('/contact')
def contact():
    return render_template("contact.html", page="contact")

@app.route('/albums')
def albums():
    return render_template('albums.html', albumImg=albumImg, page="album")

@app.route("/albums/album")
def album():
    return render_template('firstAlbum.html', portrait=portrait)


if __name__ == '__main__':
    app.run(debug=True)



