#create a memory card application
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from random import shuffle

class Question():
    def __init__ (self,quest,coranws,wong1,wong2,wong3):
        self.quest = quest
        self.coranws = coranws
        self.wong1 = wong1
        self.wong2 = wong2
        self.wong3 = wong3

questo_list = []
questo_list.append(Question("122*7 =?","854","322","435","729"))
questo_list.append(Question("bruh mean","sasid","212312","123123","12312"))
questo_list.append(Question("title3 in garimut 3","sdasd","212312","123123","12312"))
questo_list.append(Question(" who invented qwertyuiopasdfghjklzxcvbnm keyboard","Christopher Latham Sholes","212312","123123","12312"))
questo_list.append(Question("What King of China Unite china from 7 conutries?","Qin Shi Huang Di","Sui Tai Zong","Ming Dai Zong ","Tang Gao Zong"))
questo_list.append(Question("When was the Roman Defeated the Carthege","146 BC","218 BC","123 BC","318 BC"))
questo_list.append(Question("what queen of Russia that invade crimea from Ottoman Empire in 1793?","Catherine II","Anna I","Peter II","Alexander II"))
questo_list.append(Question("e^pi =?","23.140692632779269005729086367949","59.14615754178594137249564231","43.13465279184562311475465","12.34728342345345734653753645734675"))
questo_list.append(Question("(1+2.2360679774997896964091736687313)/2 = ?","1.6180339887498948482045868343656","2.03734991233246","5.1529384706","3.2438172343783447"))
questo_list.append(Question("What CPU mean?","Central Power Unit","Commander of Plugin United","Caramen Pigeon Union","Cor Pritine Union"))
questo_list.append(Question("Who founded the Continent America?","Christopher Columbus","Vasco da Gama","James Cook","Neuchartel"))
questo_list.append(Question("Whos win in the siege of Vienna?","Austria,Poland-Lithulnia,Holy Roman Empire","Ottoman","Hungary","Serbia"))
questo_list.append(Question("inpendence day of Vietnam?","2/9","2/12","1/1","10/3"))
questo_list.append(Question("sin(24) * 20","8.13473286151600415507971980683","11.934262744419280043072303339767","12.1379561375465961733172794612457295","5.2312342342342353463456456456"))
questo_list.append(Question("who caculated the perimeter of earth that very correct?","Erathosthenes","Caesar","Euler","Archimedes"))


app = QApplication([])
win = QWidget()
win.setWindowTitle('Memory Card')

# 2) Create an application object, windowed application. Set the heading and dimensions.
lb_Question = QLabel('The most diffcult question in the wolrd')
btn_OK = QPushButton('Answer')

RadioGroupBox = QGroupBox('Answer Options')

rbtn1 = QRadioButton('Option1')
rbtn2 = QRadioButton('Option2')
rbtn3 = QRadioButton('Option3')
rbtn4 = QRadioButton('Option4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox= QGroupBox('Test result')
lb_Result = QLabel('Are you correct or not?')
lb_Correct = QLabel('the answer will be here!' )

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignmentFlag.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() #question
layout_line2 = QHBoxLayout() #answer options
layout_line3 = QHBoxLayout() #button

layout_line1.addWidget(lb_Question, alignment=Qt.AlignmentFlag.AlignCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addWidget(btn_OK)


layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

win.setLayout(layout_card)
def show_res():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("nesque")
    

def show_que():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Answer")
    
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def tes():
    if btn_OK.text() == "Answer":
        show_res()
    else:
        show_que()
    
answers = [rbtn1,rbtn2,rbtn3,rbtn4]
def ask(q : Question):
    shuffle(answers)
    answers[0].setText(q.coranws)
    answers[1].setText(q.wong1)
    answers[2].setText(q.wong2)
    answers[3].setText(q.wong3)
    lb_Question.setText(q.quest)
    lb_Correct.setText(q.coranws)
    show_que()

def show_cor(res):
    lb_Result.setText(res)
    show_res()       

def check_anw():
    if answers[0].isChecked():
        show_cor("cor")
        win.score += 1
        print("staste\n -total quest:",win.total, "\n - coranw:", win.score)
        print("rating",win.score/win.total*100,"%")
    else:
        print("rating",win.score/win.total*100,"%")
        if answers[1].isChecked() or answers[2].isChecked()  or answers[3].isChecked():
            show_cor("wong") 


def nesques():
    win.total += 1
    if win.total - 1 < len(questo_list):
        ask(questo_list[win.total - 1])
    else:
        win.total -= 1
        RadioGroupBox.hide()
        AnsGroupBox.setTitle("Quiz has ended!")
        lb_Result.setText("You have answered " + str(win.score) + " out of " + str(win.total) + " questions correctly!")
        lb_Correct.setText("Your final grade is " + str(win.score/win.total * 100) + "%")
        lb_Question.hide()
        AnsGroupBox.show()


def cliok():
    if btn_OK.text() == "Answer":
        check_anw()
    else:
        nesques()
win.total = 0
win.score = 0
win.curque = -1
nesques()
btn_OK.clicked.connect(cliok)
win.show()
app.exec()