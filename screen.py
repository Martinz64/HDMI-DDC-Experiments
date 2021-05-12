import psutil

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from time import sleep
from PIL import Image, ImageFont
from pathlib import Path

serial = i2c(port= 	1, address=0x3C)
device = ssd1306(serial, rotate=0)

print ("i915 HDMI DDC - OLED display")
font_path = str(Path(__file__).resolve().parent.joinpath('pixelmix.ttf'))
font = ImageFont.truetype(font_path, 8)
font2 = ImageFont.truetype(font_path, 16)
# Box and text rendered in portrait mode
while True:

	with canvas(device) as draw:
		#draw.rectangle(device.bounding_box, outline="white", fill="black")
		#draw.text((10, 40), "Hello World", fill="white")
			draw.text((0, 0), "CPU: %i" % psutil.cpu_percent(), font=font2, fill="white")
			sleep(0.1)

#sleep(10)

#img_path = str(Path(__file__).resolve().parent.joinpath('oled_sc.bmp'))
#logo = Image.open(img_path).convert("RGBA")
#fff = Image.new(logo.mode, logo.size, (255,) * 4)

#background = Image.new("RGBA", device.size, "white")
#posn = ((device.width - logo.width) // 2, 0)
font_path = str(Path(__file__).resolve().parent.joinpath('pixelmix.ttf'))
font = ImageFont.truetype(font_path, 8)
#font2 = ImageFont.truetype(font_path, 16)

with canvas(device) as draw:
	draw.rectangle(device.bounding_box, outline="white", fill="black")
	print("posn")
	draw.text((0, 40), "CPU:", font=font, fill="white")

	while True:
		#for angle in range(0, 360, 2):
		#rot = logo.rotate(angle, resample=Image.BILINEAR)
		#img = Image.composite(rot, fff, rot)
		#background.paste(img, posn)

		#device.display(logo.convert(device.mode))
		draw.text((0, 40), "CPU:", font=font, fill="white")
		#draw.text((30, 40), "%f" % psutil.cpu_percent(), font=font2, fill="white")

		
		
		sleep(1)
