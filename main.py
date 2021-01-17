#from pythonscripts.imageprocessing import imageprocess

from PIL import Image,ImageFilter

def process_image():
    img = Image.open(r'images/sample1.png')
    #filter_image = img.filter(ImageFilter.BLUR)
    #filter_image = img.filter(ImageFilter.SMOOTH)
    #filter_image = img.filter(ImageFilter.SHARPEN)
    filter_image = img.convert('L')
    
    #filter_image.save('images/output/sample1-blur.png','png')
    #filter_image.save('images/output/sample1-smooth.png','png')
    #filter_image.save('images/output/sample1-sharpen.png','png')
    filter_image.save('images/output/sample1-gray.png','png')
#Call image processing method
process_image()


