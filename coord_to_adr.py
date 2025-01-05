from tkinter import *

import requests
from PIL import Image, ImageTk

google_api_key = "AIzaSyBv1qcwxLj3vgc0dLgwuL74xNqKeVu94_M"

longlat = "48.862725,2.287592"


api_map_google = (
    "https://maps.googleapis.com/maps/api/geocode/json?latlng="
    + longlat
    + "&key="
    + google_api_key
)

print(api_map_google)


# result = requests.get(api_map_google)
# print(result.json())
window = Tk()

image_path = "./image/Plan Bordeaux.png"
image = Image.open(image_path)
image_width, image_height = image.size

window.geometry(f"{image_width}x{image_height}")
window.resizable(False, False)
canvas = Canvas(window, width=image_width, height=image_height, bg="blue")
canvas.pack()

photo = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, image=photo, anchor="nw")

window.mainloop()
