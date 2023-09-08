# PIL - Python Imaging Library
# pip install pillow

from PIL import Image, ImageFilter

try:
    original = Image.open('python.png')
except FileNotFoundError:
    print('Файл не найден')

print('Параметры изображения:')
print('Формат:', original.format)
print('Размер:', original.size)
print('Цветовая схема:', original.mode)

blur = original.filter(ImageFilter.BLUR)
boxblur = original.filter(ImageFilter.BoxBlur(20))
gaussblur = original.filter(ImageFilter.GaussianBlur(20))
# blur.save('python_blur.png')
# boxblur.save('python_boxblur.png')
# gaussblur.save('python_gaussblur.png')

cropped = original.crop((0,0, 195// 2, 113))
cropped.save('crop.png')

contour = original.filter(ImageFilter.CONTOUR)
contour.save('contour.png')  # делаем раскраски

pixels = original.load()  # получили массив пикселей
w, h = original.size  #  получили размер переменных w и h

resized = original.resize((w//2, h//2))
resized.save('thumb.png')

for x in range(w):
    for y in range(h):
        r, g, b = pixels[x,y]
        pixels[x, y] = g, b, r




