import os
import time
import datetime
import pywintypes
from win10toast import ToastNotifier

#toast = ToastNotifier()
#toast.show_toast("WAMAC Service Manager", "Attendance extraction has been started.", duration=10)


os.chdir(r"C:\Users\ishan\Desktop\background-app")

i = 0

while False:
    i += 1
    time.sleep(1)
    with open('file.txt', 'w') as f:
        f.write(str(i))