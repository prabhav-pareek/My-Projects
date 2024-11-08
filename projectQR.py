# Making QR Code through Python Code
import pyqrcode

# String which represent the QR code
url = input(f"Paste the URL - ")
# Generate QR code
qr = pyqrcode.create(url)
# Create and save the png file naming "projectQR.png"
qr.png("projectQR.png", scale=10)
