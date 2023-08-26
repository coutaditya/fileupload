from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'  # Folder to store uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

    file_info = {
        'filename': file.filename,
        'size': os.path.getsize(filename),
        'path': filename
    }

    return jsonify({'message': 'File uploaded successfully', 'file_info': file_info})

if __name__ == '__main__':
    app.run(debug=True)
