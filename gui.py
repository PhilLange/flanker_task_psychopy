
from psychopy import gui

myDlg = gui.Dlg(title="Social Flanker Task ")
myDlg.addText('ProbandInneninformationen')
myDlg.addField('Code:')
myDlg.addField('Alter:', choices=['18','19', '20', "21", "22", "23", "24",
                                  "25", "26", "27", "28", "29", "30", "31",
               d                   "32"])
myDlg.addField('Geschlecht:', choices=['Männlich', 'Weiblich', 'Divers'])
myDlg.addField('Erste Bedingung:', choices=["Positiv ", "Negativ"])
ok_data = myDlg.show()  # show dialog and wait for OK or Cancel
if myDlg.OK:  # or if ok_data is not None
    print(ok_data)
else:
    print('abgebrochen')
