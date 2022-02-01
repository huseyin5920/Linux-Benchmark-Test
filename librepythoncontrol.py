import psutil
import pyautogui

print ("LIBREOFFICE için Kontrol ediliyor.")

process_name = "soffice"
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
                if(p.cpu_percent(interval=1.0)>50):
                    print("UYGULAMA BAŞLADI")
                    while TRUEFALSE:
                        cpuValue = p.cpu_percent(interval=1.0)
                        print("************")
                        print(cpuValue)
                        if(cpuValue<10):
                            print("XDOTOOL BAŞLAYABİLİİR")
                            pyautogui.moveTo(1870,184,duration=0.5)

                            for i in range(3):
                                pyautogui.dragTo(1870,969,duration=1)
                                pyautogui.dragTo(1870,184,duration=1)
                            pyautogui.leftClick(x=1902,y=46)
                            TRUEFALSE = False
                        else:
                            print("LIBREOFFICE ÇALIŞIYOR")

    except:
        print("UYGULAMA ÇALIŞMIYOR")
