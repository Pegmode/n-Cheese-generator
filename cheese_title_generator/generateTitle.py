import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw
import sys

DEBUG_SIZE = (500,500)#debug image size
DEFAULT_BG_COLOR = (10, 66, 123)#default win
DEFAULT_TEXT_COLOR = (0xff, 0xff, 0xff)
DEBUG_TEXT = "TOP n \nCHEESE"
DEFAULT_FONT = "cheese_title_generator\ComicNeue-Bold.ttf"

def generateCheeseText(size, text):#generate a single formatted text title
    im = Image.new("RGB", size, color = DEFAULT_BG_COLOR)
    fontSize = size[1]//5
    try:
        font = ImageFont.truetype(DEFAULT_FONT, fontSize)
    except OSError:
        sys.exit("Error: Font file \"{}\" not found".format(DEFAULT_FONT))

    imageEdit = ImageDraw.Draw(im)
    textCenterLocation = (size[0]/2, size[1]/2)
    imageEdit.multiline_text(textCenterLocation, text, DEFAULT_TEXT_COLOR, font = font, anchor = "mm", align = "center")
    return im

def generateNCheeseTitles(n, size):#generate N 
    titleText = "top {}\ncheese".format(n)
    im = generateCheeseText(size, titleText)
    im.save("title.jpg")
    for i in range(n):
        text = "number\n{}".format(i + 1)
        im =generateCheeseText(size, text)
        im.save("text{}.jpg".format(i+1))#Once we figure out how the programs give output to ffmpeg we may need to change this

def debugGenerateTiles():#debug and example usage for generating title cards
    generateNCheeseTitles(4, DEBUG_SIZE)

debugGenerateTiles()