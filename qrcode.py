import pyqrcodeng #importing pyqrcode for generating  qrcode
import pandas as pd #importing pandas to read the items in excel
from PIL import Image,ImageDraw,ImageFont #from (pillow) PIL importing Image to display image, imagedraw to write text on image,Imagefotn to change the font of an text

def createQRCode():      #defining a function and iterating through for loop to generate all the qrcodes in the excel
    df= pd.read_csv("qr.csv")#reading csv file
    for index,values in df.iterrows():
        QRcode=values["Barcode"]
        data=f'''
        QRcode:{QRcode}\n      
        '''
        image=pyqrcodeng.create(data)
        image.png(f"{QRcode}.png",scale=5)
        im = Image.open(f"{QRcode}.png") #opens the image
        logo = Image.open('logo.png')  #opens the logo
        box = (85,85,160,160) #box are (left, upper, right, lower).
        im.crop(box)
        region = logo
        region = region.resize((box[3] - box[1], box[3] - box[1])) #(image.width-logo.wigth),(image.height-logo.height)
        im.paste(region,box)
#text in image
        font = ImageFont.truetype("arial.ttf",20)
        draw = ImageDraw.Draw(im)
        (x, y) = (55,-3)
        message = "Gravton Motors"
        color = 'rgb(0,0,0)'
        draw.text((x, y), message, fill=color,font= font)
#adding qrcode num
        font2=ImageFont.truetype("arial.ttf",15)
        message = f"{QRcode}"
        (x,y)=(65,225)
        color = 'rgb(0,0,0)'
        draw.text((x, y), message, fill=color,font=font2)
        im = im.convert("RGBA")
        im.save(f"qrcodesssss/{QRcode}.png")

        # im.show()


createQRCode()














