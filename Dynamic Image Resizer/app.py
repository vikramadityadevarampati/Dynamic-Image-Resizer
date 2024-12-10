from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/resize', methods=['POST'])
def resize_image():
    try:
        # Get file and dimensions from the request
        file = request.files['image']
        width = int(request.form['width'])
        height = int(request.form['height'])

        # Open image and resize it
        image = Image.open(file)
        resized_image = image.resize((width, height))

        # Save resized image to an in-memory file
        img_io = io.BytesIO()
        resized_image.save(img_io, 'JPEG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/jpeg')

    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
