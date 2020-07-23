# File Name:     hw10Project1.py
# Programmer:    Gabe Garcia
# Date:          7/22/2020

from graphics import*
from button import*

def main():
  #create window
  win = GraphWin("Buttons", 400, 400)
  win.setBackground("white")

  #create button from Button class
  button = Button(win, Point(200, 200), 200, 50, "Click to Calculate")
  button.activate()

  #create text
  Text(Point(125, 50), "Enter father's height in inches").draw(win)
  Text(Point(130, 100), "Enter mother's height in inches").draw(win)

  #create entry boxes
  fHeightBox = Entry(Point(325, 50), 5)
  fHeightBox.setFill('lightgray')
  #fHeightBox.setText("0")
  mHeightBox = Entry(Point(325, 100), 5)
  mHeightBox.setFill('lightgray')
  #mHeightBox.setText("0")
  mHeightBox.draw(win)
  fHeightBox.draw(win)
  
  #capture click on button
  buttonClick = win.getMouse()

  #set variables for calculations
  fatherHeight = eval(fHeightBox.getText())
  motherHeight = eval(mHeightBox.getText())

  femaleHeight = ((fatherHeight * (12/13)) + motherHeight) / 2
  maleHeight = ((motherHeight * 13/12) + fatherHeight) / 2

  femaleHeightFeet = femaleHeight // 12
  femaleHeightInches = femaleHeight % 12

  maleHeightFeet = maleHeight // 12
  maleHeightInches = maleHeight % 12

  #Display output in window when button clicked
  if(button.clicked(buttonClick)):
    Text(Point(140, 260), "Female child's height: {0:0.00f} inches".format(femaleHeight)).draw(win)
    Text(Point(175, 275),"Female child's height {0:0.00f} feet and {0:0.00f} inches".format(femaleHeightFeet).format(femaleHeightInches)).draw(win)
    Text(Point(128, 300), "Male child's height: {0:0.00f} inches".format(maleHeight)).draw(win)
    Text(Point(165, 315), "Male child's height {0:0.00f} feet and {0:0.00f} inches".format(maleHeightFeet).format(maleHeightInches)).draw(win)

  win.getMouse()
  win.close()

main()

