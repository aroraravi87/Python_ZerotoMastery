#from pythonscripts.imageprocessing import imageprocess

import sys
import os
from PIL import Image,ImageFilter

def process_image():
    img = Image.open(r'images/sample2.jpg')
    #filter_image = img.filter(ImageFilter.BLUR)
    #filter_image = img.filter(ImageFilter.SMOOTH)
    #filter_image = img.filter(ImageFilter.SHARPEN)
    #filter_image = img.convert('L')
    #rotate=filter_image.rotate(180)
    #resize=filter_image.resize((300,300))
    #filter_image.save('images/output/sample1-blur.png','png')
    #filter_image.save('images/output/sample1-smooth.png','png')
    #filter_image.save('images/output/sample1-sharpen.png','png')
    #box=(400,400,600,600)
    #region=filter_image.crop(box)
    img.thumbnail((400,400))
    img.save('images/output/sample2-thumb.png','png')
    print(img.size)
    img.show()

#convert image from jpg.png
def jpgtopngconverter():
    try:
        input_folder=sys.argv[1]
        output_folder=sys.argv[2]
        print(input_folder)
 
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            
        os.chmod(input_folder,0o777)
        os.chmod(output_folder,0o777)

        for filename in os.listdir(input_folder):
            img=Image.open(f'{input_folder}{filename}')
            cleanname=os.path.splitext(filename)[0]
            img.save(f'{output_folder}{cleanname}.png','png')
            print('All done!!!')
    except:
       raise 


#Call image processing method
#process_image()
jpgtopngconverter()


