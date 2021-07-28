def distance(num1, num2, num3):
    if abs(num1 - num2) == 1 and abs(num3 - num1) >= 2:
        print("True")
    if abs(num1 - num3) == 1 and abs(num2 - num1) >= 2:
        print("True")
    if abs(num2 - num3) >= 2 and abs(num3 - num1) == 1:
        print("True")
    if abs(num3 - num2) >= 2 and abs(num2 - num1) == 1:
        print("True")
  #  else:
    #    print("false")
    if abs(num2) - abs(num1) == 0:
        print("false")
    if abs(num3) - abs(num1) == 0:
        print("false")
    if abs(num2) - abs(num3) == 0:
        print("false")
    
distance (11,1,10)
