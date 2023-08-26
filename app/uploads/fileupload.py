from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'  # Folder to store uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
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
    else:
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
