from tkinter import Tk, filedialog, Label
from PIL import Image, ImageDraw, ImageFont, ImageTk

filename = filedialog.askopenfilename(initialdir=r"C:\Users\ASUS\Downloads", title="Select an Image : ")


def add_watermark(image, wm_text):
    opened_image = Image.open(image)
    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)
    font_size = int(image_width / 8)
    font = ImageFont.truetype('arial.ttf', font_size)
    x, y = int(image_width / 2), int(image_height / 2)
    draw.text((x, y), wm_text, font=font, fill="#FFF", stroke_fill="#222", anchor="ms")
    return opened_image


result_image = add_watermark(filename, 'My Watermark')

screen = Tk()
screen.title("Watermark App")
result_photo = ImageTk.PhotoImage(result_image)
result_label = Label(screen, image=result_photo)
result_label.pack()

screen.mainloop()
