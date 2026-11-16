import qrcode
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Your GitHub URL
url = "https://github.com/DeveshPrajapat"

# --- Step 1: Generate QR code ---
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# --- Step 2: Add GitHub logo ---
logo_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
response = requests.get(logo_url)
logo = Image.open(BytesIO(response.content)).convert("RGBA")

# Resize logo (max 20% of QR code size)
qr_width, qr_height = qr_img.size
logo_size = int(qr_width * 0.2)
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Prepare mask from alpha channel
mask = logo.split()[3]

# Paste logo at center
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
qr_img.paste(logo, pos, mask=mask)

# --- Step 3: Add text at bottom ---
text = "GitHub"
font_size = 20
try:
    font = ImageFont.truetype("arial.ttf", font_size)
except:
    font = ImageFont.load_default()

# Use ImageDraw to get text size
dummy_draw = ImageDraw.Draw(qr_img)
text_bbox = dummy_draw.textbbox((0,0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Create new image with extra space for text
new_height = qr_height + text_height + 10  # 10 pixels padding
new_img = Image.new("RGB", (qr_width, new_height), "white")
new_img.paste(qr_img, (0,0))

# Draw text
draw = ImageDraw.Draw(new_img)
draw.text(((qr_width - text_width)//2, qr_height + 5), text, fill="black", font=font)

# --- Step 4: Show and save QR code ---
new_img.show()
new_img.save("github_qr_with_logo_and_text.png")
print("QR code with logo and text saved as github_qr_with_logo_and_text.png")
