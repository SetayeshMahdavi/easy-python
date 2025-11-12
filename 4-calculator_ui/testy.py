from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

window = uic.loadUi("calculator.ui")  
window.lineEdit.setReadOnly(True)
window.show()


result = []  

# def fun():
#     obj = window.sender()            
#     result.append(obj.text())         
#     window.lineEdit.setText("".join(result)) 
#     print(result)          

def fun():
    obj = window.sender()
    text = obj.text()
    ops = {"+", "-", "*", "/", "."}
    if result and result[-1] in ops and text in ops:
        return 
    result.append(text)
    window.lineEdit.setText("".join(result))
    print(result)


def give_result():
    try:
        m = "".join(result)            
        r = eval(m)                   
        window.lineEdit.setText(str(r))
        result.clear()               
        result.append(str(r))       
    except:
        window.lineEdit.setText("Error")
        result.clear()

def clear_all():
    result.clear()
    window.lineEdit.clear()

# window.pushButton_0.clicked.connect(fun)
# window.pushButton_1.clicked.connect(fun)
# window.pushButton_2.clicked.connect(fun)
# window.pushButton_3.clicked.connect(fun)
# window.pushButton_4.clicked.connect(fun)
# window.pushButton_5.clicked.connect(fun)
# window.pushButton_6.clicked.connect(fun)
# window.pushButton_7.clicked.connect(fun)
# window.pushButton_8.clicked.connect(fun)        
# window.pushButton_9.clicked.connect(fun)


for i in range(10):
    butt=getattr(window,f"pushButton_{i}")
    butt.clicked.connect(fun)


# window.pushButton_plus.clicked.connect(fun)
# window.pushButton_minus.clicked.connect(fun)
# window.pushButton_mul.clicked.connect(fun)    
# window.pushButton_div.clicked.connect(fun)
# window.pushButton_dot.clicked.connect(fun)


names=["plus","minus","mul","div","dot"]
for i in names:
    butt2=getattr(window,f"pushButton_{i}")
    butt2.clicked.connect(fun)


window.pushButton_equal.clicked.connect(give_result)
window.pushButton_clear.clicked.connect(clear_all)


sys.exit(app.exec())
