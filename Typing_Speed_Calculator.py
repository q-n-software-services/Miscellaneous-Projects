import time
x = input("\t\t\t Press ENTER to start the TIMER")
print('   ')
for i in [3, 2, 1]:
    print("\t\t\t\t\t\t", i)
    print("   ")
    time.sleep(1)
waqt1 = time.time()
matan = input("\t\t\t\tTYPE as much as YOU can\t\t\n\n\t")
waqt2 = time.time()
alfaz = matan.split()
lafz_count = len(alfaz)
waqt_total = waqt2 - waqt1
waqt_total = waqt_total / 60
speed = lafz_count / waqt_total
raftar_int = int(speed)
print("   ")
print("   ")
print("\tyour typing speed is :\t", raftar_int, " wpm\t\ti.e. (", speed, " wpm)")
print("   ")
print("   ")
print("   ")
print("   ")
print("   ")
y = input()
