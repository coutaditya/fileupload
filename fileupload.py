from flask import Flask, request, jsonify, render_template
import os
import datetime
import magic

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'  # Folder to store uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_file_description(file_path):
    try:
        magic_obj = magic.Magic()
        file_type = magic_obj.from_file(file_path)
        return file_type
    except Exception as e:
        return str(e)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filename)
    file_desc = get_file_description(filename)

    file_info = {
        'filename': file.filename,
        'size': os.path.getsize(filename),
        'path': filename,
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'description': file_desc
    }

    return jsonify({'message': 'File uploaded successfully', 'file_info': file_info})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
