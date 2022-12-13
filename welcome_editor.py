from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter


###### Ordenar todo esto pls #######

def img_editor_text(text_author):

    ##### Sizes, Font and Img ####

    x1 = 450
    y1 = 100
    
    text_author = text_author.replace(" ", "")
   

    size_text = len(str(text_author))

    x2 = 670-size_text*12

    y2 = 175

    
    img = Image.open("./Img/welcome.png")
    ##img = Image.new("RGB", (1024, 500), (91,68,130))

    image_avatar = Image.open("./Avatar/avatar.png")

    new_width  = 200
    new_height = 200
    image_avatar = image_avatar.resize((new_width, new_height), Image.ANTIALIAS)

    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("./Fonts/golong.ttf", 80)
    # draw.text((x, y),"Sample Text",(r,g,b))
    font2 = ImageFont.truetype("./Fonts/golong.ttf", 50)

    text_welcome = "Bienvenido/a"
    shadowcolor = "white"


    #### Text and text-shadow ####

    ### Border White ###
    draw.text((x1-1, y1), text_welcome, font=font, fill=shadowcolor)
    draw.text((x1+1, y1), text_welcome, font=font, fill=shadowcolor)
    draw.text((x1, y1-1), text_welcome, font=font, fill=shadowcolor)
    draw.text((x1, y1+1), text_welcome, font=font, fill=shadowcolor)


    draw.text((x1-1, y1-1), text_welcome, font=font, fill=shadowcolor)
    draw.text((x1+1, y1-1), text_welcome, font=font, fill=shadowcolor)
    draw.text((x1-1, y1+1), text_welcome, font=font, fill=shadowcolor)
    draw.text((x1+1, y1+1), text_welcome, font=font, fill=shadowcolor)

    ### Border White ###
    draw.text((x2-1, y2), text_author, font=font2, fill=shadowcolor)
    draw.text((x2+1, y2), text_author, font=font2, fill=shadowcolor)
    draw.text((x2, y2-1), text_author, font=font2, fill=shadowcolor)
    draw.text((x2, y2+1), text_author, font=font2, fill=shadowcolor)

    # thicker border
    draw.text((x2-1, y2-1), text_author, font=font2, fill=shadowcolor)
    draw.text((x2+1, y2-1), text_author, font=font2, fill=shadowcolor)
    draw.text((x2-1, y2+1), text_author, font=font2, fill=shadowcolor)
    draw.text((x2+1, y2+1), text_author, font=font2, fill=shadowcolor)


    """blurred = Image.new('RGBA', img.size)
    draw = ImageDraw.Draw(blurred)
    draw.text(xy=(x1+220,y1+65), text=text_welcome, fill='black', font=font, anchor='ms')
    blurred = blurred.filter(ImageFilter.BoxBlur(7))


    img.paste(blurred,blurred)

    blurred = Image.new('RGBA', img.size)
    draw = ImageDraw.Draw(blurred)
    draw.text(xy=(x2+size_text*15,y2+45), text=text_author, fill='black', font=font2, anchor='ms')
    blurred = blurred.filter(ImageFilter.BoxBlur(7))

    img.paste(blurred,blurred)

    draw = ImageDraw.Draw(img)"""


    draw.text(xy=(x1,y1),text=text_welcome,fill=(219,214,230),font=font)

    draw.text(xy=(x2,y2),text=text_author,fill=(134,205,255),font=font2)


    ############ Avatar #############

    widht, height = image_avatar.size

    mask_im = Image.new("L", image_avatar.size, 0)
    draw = ImageDraw.Draw(mask_im)
    draw.ellipse((20, 20, widht-20, height-20), fill=255, outline="white")
    mask_im.save('./Img/mask_circle.jpg', quality=95)

    mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(1))

    #add background to image_avatar

    sample = Image.new("RGB", (new_width, new_height))
    border = ImageDraw.Draw(sample)  
    border.ellipse((0, 0, widht, height), fill = (219,214,230))
    

    sample.paste(image_avatar, (0, 0), mask_im_blur)


    mask_im2 = Image.new("L", image_avatar.size, 0)
    draw = ImageDraw.Draw(mask_im2)
    draw.ellipse((14, 14, widht-14, height-14), fill=255)

    mask_im_blur_2 = mask_im2.filter(ImageFilter.GaussianBlur(1))

    img.paste(sample, (560, 220), mask_im_blur_2)
    
    ##### Save image #####

    img.save("./Img/welcome_edit.png")

