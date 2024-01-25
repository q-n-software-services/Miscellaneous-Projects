import calendar
Saal = input("Enter year in the specified format  YYYY      ")
Saal = int(Saal)
print()
Mahina = input("Enter month in the specified format  MM     ")
print()
Mahina = int(Mahina)
tareekh = input("Enter date in the specified format  DD     ")
print()
tareekh = int(tareekh)
print()
print()
din = calendar.weekday(Saal, Mahina, tareekh)
if din == 0:
    print("                         Monday")
elif din == 1:
    print("                          Tuesday")
elif din == 2:
    print("                         Wednesday")
elif din == 3:
    print("                         Thursday")
elif din == 4:
    print("                         Friday")
elif din == 5:
    print("                         Saturday")
elif din == 6:
    print("                         Sunday")

print()
print()
print()
print()
print()
x = input("enter any character to terminate the program")

