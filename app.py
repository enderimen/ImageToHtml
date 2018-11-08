from flask import Flask, render_template
from PIL import Image
import os

app = Flask(__name__)
app.config["DEBUG"] = True;

PUBLIC_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = PUBLIC_FOLDER

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process')
def process():

    target = os.path.join(app.config['UPLOAD_FOLDER'], "superfans.png")
    im = Image.open(target)  # Can be many different formats.
    width, height = im.size

    # width x height multidimensional array
    colorArray = [[0 for j in range(height)] for i in range(width)]

    rgb_im = im.convert('RGB')

    for pixel_x in range(0, width):
        for pixel_y in range(0, height):
            r, g, b = rgb_im.getpixel((pixel_x, pixel_y))
            colorArray[pixel_x][pixel_y] = r, g, b

    return render_template("index.html", width = width, height = height, colorArray = colorArray)

if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)