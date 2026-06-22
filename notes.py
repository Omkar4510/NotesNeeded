# This project tells you how many notes you need. 

value = (input("enter the amount : "))

no_500_notes= 0
no_100_notes= 0
no_50_notes = 0
no_20_notes = 0
no_10_notes = 0
no_1_coins = 0

if value.isdigit():
    value= int(value)
    no_500_notes = value // 500
    value = value% 500 

    no_100_notes = value // 100
    value = value% 100 

    no_50_notes= value //50
    value =value%50

    no_20_notes = value // 20
    value = value% 20 

    no_10_notes = value//10
    value = value %10

    no_2_coins = value//2
    value = value %2

    no_1_coins = value//1
    value = value %1

    print(" You need :")
    print(str(no_500_notes) + " x ₹500 notes")
    print(str(no_100_notes) + " x ₹100 notes")
    print(str(no_50_notes) + " x ₹50 notes")
    print(str(no_20_notes) + " x ₹20 notes")
    print(str(no_10_notes) + " x ₹10 notes")
    print(str(no_2_coins) + " x ₹2 Coins")
    print(str(no_1_coins) + " x ₹1 Coins")
else:
    print(f"{value} is not a number !")