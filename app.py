from flask import Flask, request, render_template, send_file
import os
from stegosafe import encode_message, decode_message
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
@app.route('/')
def home():
    return render_template('frontend.html')
@app.route('/process', methods=['POST'])
def process():
    action = request.form.get("action")
    uploaded_file = request.files.get("image")
    if not uploaded_file:
        return "No file uploaded", 400
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
    uploaded_file.save(file_path)
    if action == "encode":
        message = request.form.get("message", "")
        if not message:
            return "No message provided for encoding", 400
        output_path = os.path.join(OUTPUT_FOLDER, "encoded_" + uploaded_file.filename)
        encode_message(file_path, message, output_path)
        return send_file(output_path, as_attachment=True)
    elif action == "decode":
        decoded_message = decode_message(file_path)
        # Pass the decoded message to the template
        return render_template('result.html', decoded_message=decoded_message)
    else:
        return "Invalid action", 400
if __name__ == '__main__':
    app.run(debug=True)
