import sys


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWizardPage, QGroupBox, QGridLayout, QButtonGroup, QRadioButton, QTreeWidget, QTreeWidgetItem


class FundamentalTraitsPage(QWizardPage):

    def __init__(self, *args, **kwargs):
        super(FundamentalTraitsPage, self).__init__(*args, **kwargs)

        # data entry widgets
        # name
        namebox = QGroupBox("Name")

        # player vs. npc
        playerBox = QGroupBox("Player Controlled")
        playerLayout = QGridLayout()
        self.playerGroup = QButtonGroup()
        playerPcButton = QRadioButton("Player Character")
        playerNpcButton = QRadioButton("Non-Player Character")
        self.playerGroup.addButton(playerPcButton)
        self.playerGroup.addButton(playerNpcButton)
        playerLayout.addWidget(playerPcButton, 1, 1)
        playerLayout.addWidget(playerNpcButton, 2, 1)
        playerBox.setLayout(playerLayout)

        # gender
        genderBox = QGroupBox("Gender")
        genderLayout = QGridLayout()
        self.genderGroup = QButtonGroup()
        genderFemaleButton = QRadioButton("Female")
        genderMaleButton = QRadioButton("Male")
        genderOtherButton = QRadioButton("Other")
        self.genderGroup.addButton(genderFemaleButton)
        self.genderGroup.addButton(genderMaleButton)
        self.genderGroup.addButton(genderOtherButton)
        genderLayout.addWidget(genderFemaleButton, 1, 1)
        genderLayout.addWidget(genderMaleButton, 2, 1)
        genderLayout.addWidget(genderOtherButton, 3, 1)
        genderBox.setLayout(genderLayout)

        # age
        ageBox = QGroupBox("Age")
        ageLayout = QGridLayout()
        self.ageGroup = QButtonGroup()
        ageYouthButton = QRadioButton("Young")
        ageAdultButton = QRadioButton("Adult")
        ageMiddleButton = QRadioButton("Middle Aged")
        ageElderButton = QRadioButton("Elderly")
        self.ageGroup.addButton(ageYouthButton)
        self.ageGroup.addButton(ageAdultButton)
        self.ageGroup.addButton(ageMiddleButton)
        self.ageGroup.addButton(ageElderButton)
        ageLayout.addWidget(ageYouthButton, 1, 1)
        ageLayout.addWidget(ageAdultButton, 2, 1)
        ageLayout.addWidget(ageMiddleButton, 3, 1)
        ageLayout.addWidget(ageElderButton, 4, 1)
        ageBox.setLayout(ageLayout)

        # income
        incomeBox = QGroupBox("Income")
        incomeLayout = QGridLayout()
        self.incomeGroup = QButtonGroup()
        incomePoorButton = QRadioButton("Impoverished")
        incomeLowButton = QRadioButton("Lower Class")
        incomeMiddleButton = QRadioButton("Middle Class")
        incomeUpperButton = QRadioButton("Upper Class")
        incomeRichButton = QRadioButton("Fabulously Wealthy")
        self.incomeGroup.addButton(incomePoorButton)
        self.incomeGroup.addButton(incomeLowButton)
        self.incomeGroup.addButton(incomeMiddleButton)
        self.incomeGroup.addButton(incomeUpperButton)
        self.incomeGroup.addButton(incomeRichButton)
        incomeLayout.addWidget(incomePoorButton, 1, 1)
        incomeLayout.addWidget(incomeLowButton, 2, 1)
        incomeLayout.addWidget(incomeMiddleButton, 3, 1)
        incomeLayout.addWidget(incomeUpperButton, 4, 1)
        incomeLayout.addWidget(incomeRichButton, 5, 1)
        incomeBox.setLayout(incomeLayout)

        # overall layout
        fullLayout = QGridLayout()
        fullLayout.addWidget(namebox, 1, 1)
        fullLayout.addWidget(playerBox, 2, 1)
        fullLayout.addWidget(genderBox, 3, 1)
        fullLayout.addWidget(ageBox, 4, 1)
        fullLayout.addWidget(incomeBox, 5, 1)
        self.setLayout(fullLayout)

    def isComplete(self) -> bool:
        return super().isComplete()

class SimpleListPage(QWizardPage):

    def __init__(self, *args, **kwargs):
        super(SimpleListPage, self).__init__(*args, **kwargs)

class MutexListPage(QWizardPage):

    def __init__(self, *args, **kwargs):
        super(MutexListPage, self).__init__(*args, **kwargs)

class TreePage(QWizardPage):

    def __init__(self, *args, **kwargs):
        super(TreePage, self).__init__(*args, **kwargs)

        treeBox = QGroupBox()
        treeLayout = QGridLayout()
        treeBase = QTreeWidget()
        treeBase.setColumnCount(3)
        treeFamily = QTreeWidgetItem(treeBase)
        treeFamily.setText(0, "Family")
        treeFamilyParental = QTreeWidgetItem(treeFamily)
        treeFamilyParental.setText(0, "Parental")
        treeFamilyParentalParent = QTreeWidgetItem()
        treeFamilyParentalParent.setText(0, "Parent")
        treeFamilyParentalChild = QTreeWidgetItem()
        treeFamilyParentalChild.setText(0, "Child")
        treeFamilySibling = QTreeWidgetItem(treeFamily)
        treeFamilySibling.setText(0, "Sibling")
        treeFamilySiblingSibling = QTreeWidgetItem()
        treeFamilySiblingSibling.setText(0, "Sibling")
        treeLayout.addWidget(treeBase)
        self.setLayout(treeLayout)



def main():
    app = QtWidgets.QApplication()
    
    wizzzard = QtWidgets.QWizard()
    wizzzard.addPage(FundamentalTraitsPage())
    wizzzard.addPage(TreePage())
    wizzzard.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()