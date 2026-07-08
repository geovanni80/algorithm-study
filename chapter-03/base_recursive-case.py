def regressive(i):
    print(i)
    if i <= 1:
        return
    else:
        regressive(i-1)

regressive(4)

#First interaction
    # Output = 4
    # 4 <= 1 False
    # Regressive = 3
#Second interaction
    # Output = 3
    # 3 <= 1 False
    # Regressive = 2
#Third interaction
    # Output = 2
    # 2 <= 1 False
    # Regressive = 1
#Fourth interaction
    # Output = 1
    # 1 <= 1 True
    # Return

#Finish code