from flask import Flask, request, jsonify, send_file, render_template
import pyqrcode
import io

app = Flask(__name__, static_folder='.', template_folder='.')

# Route to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qr-generator', methods=['POST'])
def QRgenerator():
    try:
        # Get the text or URL from the request
        data = request.json.get('text')
        if not data:
            return jsonify({"error": "No text provided"}), 400
        
        # Generate the QR code
        qr = pyqrcode.create(data)
        
        # Save the QR code to a BytesIO stream (in-memory)
        buffer = io.BytesIO()
        qr.png(buffer, scale=10)
        buffer.seek(0)
        
        # Return the QR code as a response
        return send_file(
            buffer,
            mimetype='image/png',
            as_attachment=False,  # Set to True if you want to force download
            download_name="qr_code.png"
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)