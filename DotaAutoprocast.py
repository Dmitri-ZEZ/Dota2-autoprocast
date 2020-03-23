import ctypes
import time
import keyboard
import pyautogui 
import pyfiglet

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def start():
    ascii_banner = pyfiglet.figlet_format("AutoProkast")
    print(ascii_banner)



def print_pressed_keys(e):
    if e.name == "q" and e.event_type == "down":
        boolInputProcast = False
        print("Ввод закончен")
        
    for command in dictionaryProcast:
        if command:
            if e.name == command[0] and e.event_type == "down":

                position = pyautogui.position()

                for x in command[1]:
                    if x=='4':
                        time.sleep(0.8)
                        PressKey(dictionaryNow[x])
                        ReleaseKey(dictionaryNow[x])
                    elif x=='5' or x=='6' or x=='z' or x=='x' or x=='c':
                        pyautogui.moveTo(position)

                        PressKey(dictionaryNow[x])
                        ReleaseKey(dictionaryNow[x])

                        pyautogui.click(button='left')
                        time.sleep(0.01)
                    else:
                        PressKey(dictionaryNow[x])
                        ReleaseKey(dictionaryNow[x])
            


start()

dictionary1 = {'1': 0x02, '2': 0x3, '3': 0x04, '4': 0x05, '5': 0x06, '6': 0x07, "z": 0x2c}
dictionary2 = {'1': 0x10, '2': 0x11, '3': 0x12, '4': 0x13, '5': 0x14, '6': 0x15}
dictionaryNow = {'1': 0x02, '2': 0x3, '3': 0x04, '4': 0x05, '5': 0x06, '6': 0x07, "z": 0x2c}


dictionaryProcast = [[]]
numberProcast = 0
print("Сколько прокастов планируется ввести?")
ch = int(input())

for c in range(ch):
    print("Введите кнопку для прокаста")
    but = input()
    dictionaryProcast[numberProcast].append(but)

    print("Введите прокаст")
    procast = list(map(str, input()))
    dictionaryProcast[numberProcast].append(procast)

    numberProcast+=1
    dictionaryProcast.append([])
    print("Нажмите любую клавишу")

    input()


    



#kast1 = [2,2,1,4,2,2,2,4,6,5,3,3,2,4,5] #ветер, минус мана и метеор
#kast2 = ["z",3,3,2,4,6,5,1,2,3,4,5]

keyboard.hook(print_pressed_keys)
keyboard.wait()




                                                                      
                                                                      


