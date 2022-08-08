from captcha.image import ImageCaptcha

# image size
image = ImageCaptcha(width = 300, height = 100)

# text captcha
captcha_text = input("Enter captcha text :")

data = image.generate(captcha_text)
image.write(captcha_text, 'E:\CAPTCHA1.png')
from PIL import Image

Image.open('E:\CAPTCHA.png')