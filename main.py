# File Name:     hw7Project2.py
# Programmer:    Gabe Garcia
# Date:          7/8/2020

def main():
  fatherHeight = eval(input("Enter father's height in inches: "))
  motherHeight = eval(input("Enter mother's height in inches: "))

  femaleHeight = ((fatherHeight * (12/13)) + motherHeight) / 2
  maleHeight = ((motherHeight * 13/12) + fatherHeight) / 2

  femaleHeightFeet = femaleHeight // 12
  femaleHeightInches = femaleHeight % 12

  maleHeightFeet = maleHeight // 12
  maleHeightInches = maleHeight % 12

  print("\nFemale child's height: {0:0.00f}".format(femaleHeight))
  print("Female child's height {0:0.00f}".format(femaleHeightFeet),"feet and {0:0.00f}".format(femaleHeightInches),"inches.\n")
  print("Male child's height: {0:0.00f}".format(maleHeight))
  print("Male child's height {0:0.00f}".format(maleHeightFeet),"feet and {0:0.00f}".format(maleHeightInches),"inches.")


main()

