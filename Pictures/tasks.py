#навыки

from PIL import Image
im = Image.open("cat.jpg")
im
im.size
im1 = im.crop((100,200,700,700))
im1
im2 = im.resize((300,135))
im2 = im2.rotate(30)
im2.copy()
im.paste(im2,(0,0))
im

#задание 3

def grey_pic(start_adress,end_adress):
    img = Image.open(start_adress,mode = 'r')
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pix = img.getpixel((i,j))
            new_pix = round((pix[0] + pix[1] + pix[2])/3)
            img.putpixel((i,j),(new_pix,new_pix,new_pix))
    img.save(end_adress, "JPEG")
grey_pic("/content/cat.jpg","/content/ress.jpg")

#задание 4

from PIL import ImageDraw
#функция поучает на вход str и делает из нее картинку
def viz_text(text):
    xy = []
    for i in range(len(text)):
        xy.append((40*i,ord(text[i])))

    img = Image.new("RGB", (max(xy)[0]+100,1300), (0,0,0))
    draw = ImageDraw.Draw(img)
    for i in range(len(xy)):
        fill = (xy[i][1],xy[i][1]+4,xy[i][1]//2)
        draw.line([xy[i-1],xy[i]],fill)
    return img

viz_text('Если есть силы, можно сделать что-нибудь интересное. Придумайте что-то и сделайте это с помощью библиотеки Pillow.Если вы не уверены, годится ли ваша идея -- спросите :)')
#viz_text('Hello world')

#задание 8

def alfa_pic(start_adress,end_adress):
    img = Image.open(start_adress,mode = 'r')
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pix = img.getpixel((i,j))
            if pix[:3] == [0,0,0] or pix[:3] == [1,1,1]:
                 img.putpixel((i,j), [0,0,0,0])
    img.save(end_adress, "PNG")

