
from simpletk import *
def doCalc ( event ):

    expr = Input.text # прочитать выражение

    x = Calc ( expr ) # вычислить

    Answers.insert ( 0, expr + "=" + str(x) )

    if not Input.findItem ( expr ):

        Input.addItem ( expr )
app = TApplication ( "Калькулятор" )
app.size = (500, 200)
Input = TComboBox ( app, values = [],
height = 20 )
Input.align = "top"
Input.text = ""
Answers = TListBox ( app, values = [] )
Answers.align = "client"
Input.bind ( "<Key-Return>", doCalc )
app.run()
