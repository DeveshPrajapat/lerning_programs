import qrcode
from PIL import Image
import requests
from io import BytesIO

# Your GitHub URL
url = "https://github.com/DeveshPrajapat"

# --- Step 1: Generate QR code ---
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# --- Step 2: Add GitHub logo ---
# Load logo from URL
logo_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
response = requests.get(logo_url)
logo = Image.open(BytesIO(response.content)).convert("RGBA")  # Convert to RGBA

# Resize logo (max 20% of QR code size)
qr_width, qr_height = qr_img.size
logo_size = int(qr_width * 0.2)
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Prepare mask from alpha channel
mask = logo.split()[3]  # Alpha channel

# Calculate position to paste logo at center
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
qr_img.paste(logo, pos, mask=mask)

# --- Step 3: Show and save QR code ---
qr_img.show()
qr_img.save("github_qr_with_logo.png")
print("QR code with GitHub logo saved as github_qr_with_logo.png")
