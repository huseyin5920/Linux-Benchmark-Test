import psutil
import pyautogui

print ("FREECAD için Kontrol ediliyor.")

process_name = "freecad"
pid = None

TRUEFALSE = True
while TRUEFALSE:

    try:
        for proc in psutil.process_iter():
            if process_name in proc.name():
                pid = proc.pid
                print(pid)
                p = psutil.Process(pid)
                print(p.cpu_percent(interval=1.0))
                if(p.cpu_percent(interval=1.0)>10):
                    print("UYGULAMA BAŞLADI")
                    while TRUEFALSE:
                        cpuValue = p.cpu_percent(interval=1.0)
                        print("************")
                        print(cpuValue)
                        if(cpuValue<1):
                            print("XDOTOOL BAŞLAYABİLİİR")
                            
                            pyautogui.leftClick(x=1840,y=178)
                            pyautogui.leftClick(x=1769,y=247)
                            pyautogui.leftClick(x=1838,y=317)
                            pyautogui.leftClick(x=1908,y=245)
                            pyautogui.leftClick(x=1902,y=46)
                            TRUEFALSE = False
                        else:
                            print("FREECAD ÇALIŞIYOR")

    except:
        print("UYGULAMA ÇALIŞMIYOR")
