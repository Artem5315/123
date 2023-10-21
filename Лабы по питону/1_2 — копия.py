from simpletk import *
app = TApplication ( "Просмотр рисунков" )
app.position = (300, 100)
app.size = (1000, 620)
panel = TPanel ( app,relief = "raised",height = 40,bd = 1 )
panel.align = "top"

centerCb = TCheckBox ( panel,text = "В центре" )
centerCb.position = (150, 5)
image = TImage ( app, bg = "white" )
image.align = "client"
list1=TComboBox(app, values=['C:\Users\Asus\Desktop\dlya-samogo-luchshego-uchitelya-2668832 (1).gif',
                            'C:\Users\Asus\Desktop\dlya-samogo-luchshego-uchitelya-2668832 (1).gif',
                            'C:\Users\Asus\Desktop\dlya-samogo-luchshego-uchitelya-2668832 (1).gif',
                            'C:\Users\Asus\Desktop\dlya-samogo-luchshego-uchitelya-2668832 (1).gif',
                            'C:\Users\Asus\Desktop\dlya-samogo-luchshego-uchitelya-2668832 (1).gif'],height = 30 )
list1.position = (5, 5)
def openf(sender):
    fname=list1.text
    if fname:
        image.picture = fname
        
list1.onClick=openf

def cbChanged ( sender ):
    image.center = sender.checked
    image.redrawImage()
centerCb.onChange = cbChanged
app.run()
