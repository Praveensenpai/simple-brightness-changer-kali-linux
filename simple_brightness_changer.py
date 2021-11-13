import os
print("Brightness Value from 0.10 to 1 or 2\n")
while(1):
    try:
        n = input("Brightness Value = ")
        p = "xrandr --output HDMI-1 --brightness " + str(n)
        os.system(p)
        print("Brightness successfully changed to " + str(n) + "\n")
    except:
        pass