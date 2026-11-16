import webbrowser
from tkinter import *
from PIL import ImageTk, Image

def open_github():
    webbrowser.open("https://github.com/DeveshPrajapat")

root = Tk()
root.title("Clickable Bubble QR")

# Load QR image
img = Image.open("github_qr_with_logo_and_text.png").resize((250, 250))
qr = ImageTk.PhotoImage(img)

# Create bubble button
bubble = Button(root, image=qr, bd=0, command=open_github)
bubble.pack(pady=20)

# -------- SAVE THE SAME IMAGE -----------
img.save("bubble_qr_image.png")
print("Saved as bubble_qr_image.png")

root.mainloop()
