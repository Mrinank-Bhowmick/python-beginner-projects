from flask import Flask, request, send_file
from convert import convert_webp_to_png, convert_webp_to_svg
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def home():
    return '''
        <h1>Convert WEBP to PNG or SVG</h1>
        <form method="POST" enctype="multipart/form-data" action="/convert">
            <input type="file" name="file"><br><br>
            <select name="format">
                <option value="png">PNG</option>
                <option value="svg">SVG</option>
            </select><br><br>
            <input type="submit" value="Convert">
        </form>
    '''


@app.route('/convert', methods=['POST'])
def convert_image():
    file = request.files['file']
    output_format = request.form['format']

    if file and output_format:
        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(input_path)

        if output_format == 'png':
            output_path = input_path.replace('.webp', '.png')
            convert_webp_to_png(input_path, output_path)
        elif output_format == 'svg':
            output_path = input_path.replace('.webp', '.svg')
            convert_webp_to_svg(input_path, output_path)

        return send_file(output_path, as_attachment=True)

    return "Failed to convert"


if __name__ == '__main__':
    app.run(debug=True)
