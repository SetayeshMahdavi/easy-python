from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

window = uic.loadUi("calculator.ui") 
window.lineEdit.setReadOnly(True)
window.show()

result = []

def fun ():
    obj=window.sender()
    txt=obj.text()
    ops={"+", "-", "*", "/", "."}
    if result and result[-1] in ops and txt in ops :
        return "eror"
    result.append(txt)
    window.lineEdit.setText("".join(result))
    print(result)


def give_res ():
    try:
        m="".join(result)
        r=eval(m)
        window.lineEdit.setText(str(r))
        result.clear()
        result.append(str(r))
    except:
        window.lineEdit.setText("eror")
        result.clear()

def clear_all ():
    result.clear()
    window.lineEdit.clear()


for i in range(10):
    butt=getattr(window,f"pushButton_{i}")
    butt.clicked.connect(fun)


names=["plus","minus","mul","div","dot"]
for i in names:
    butt2=getattr(window,f"pushButton_{i}")
    butt2.clicked.connect(fun)

window.pushButton_equal.clicked.connect(give_res)
window.pushButton_clear.clicked.connect(clear_all)


sys.exit(app.exec())
