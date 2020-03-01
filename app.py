from flask import Flask, render_template, url_for

app = Flask(__name__)

albumImg = ["../static/Pictures/_DSC1002_edited-2.jpg","../static/Pictures/_DSC0900_edited-2.jpg" , '../static/Pictures/IMG_20190602_150420955.jpg',"../static/Pictures/IMG_1191.JPG",
    "../static/Pictures/IMG_1190.JPG" ,"../static/Pictures/DSC_0930.jpg"]

ImgPerCol = len(albumImg) // 3

@app.route('/')
def hello_soen287():
    return render_template("Home.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/albums')
def albums():
    return render_template('albums.html', albumImg=albumImg, ImgPerCol=ImgPerCol)


if __name__ == '__main__':
    app.run(debug=True)



