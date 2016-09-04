#python 3.4  pillow lib 
#encoding = utf-8
from PIL import Image
from PIL import ImageFont,ImageDraw
#color (0,0,0) locate [lefttop,righttop,rightbottom,leftbottom] 中文必须为unicode
def add_watermarks(inputname,outputname,wartermark,color,fontsize=24,rotate=0,locate='lefttop'):
    assert(fontsize>0)
    im=Image.open(inputname)
    p = Image.new('RGB', im.size, (255,255,255))
    p.paste(im,(0, 0, im.size[0], im.size[1]), im)
    '''
    im = Image.open("C:/Users/Leo/Desktop/Pic/513174045073095280.jpg")
    im.thumbnail((45,45))
    '''
    #im.fill('white')
    # draw=ImageDraw.Draw(p)
    #字体
    font = ImageFont.truetype('C:\Windows\Fonts\STCAIYUN.TTF', fontsize) 
    txt=Image.new('RGBA', font.getsize(wartermark))
    d = ImageDraw.Draw(txt)
    d.text((0, 0), wartermark,  font=font, fill=color)
    #旋转
    w=txt.rotate(rotate,expand=1)
    
    if w.size[0]>p.size[0] or w.size[1]>p.size[1]:
        print('water mark is too large')
    if locate == 'lefttop':
        p.paste(w,(0, 0),w)
    elif locate == 'righttop':
        p.paste(w,(p.size[0]-w.size[0],0),w)
    elif locate == 'rightbottom':
        p.paste(w,(im.size[0]-w.size[0],im.size[1]-w.size[1]),w)
    elif locate == 'leftbottom':
        p.paste(w,(0, im.size[1]-w.size[1]),w)
    else:
        print('input location error!')
        return
    p.show()
    p.save(outputname,'JPEG')
if __name__ == '__main__':
    add_watermarks('ooopic_1471486626.ico','123.jpg',u'忍','green',fontsize=24,rotate=-17.5,locate='righttop')

# x=136
# y=76
#  
# c = Image.new("RGB",(x,y))
#  
# for i in range (0,x):
#     for j in range (0,y):
#         c.putpixel([i,j],(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
#  
# c.show()
# c.save("c.png")
#im.show()