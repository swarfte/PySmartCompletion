import pynput.keyboard as pk
import PSCTool.KBFunction as PF

def on_press(key):#按下按鍵時執行
    try:
        print(f"按下了 {key.char} 鍵")
    except AttributeError: # 特殊按鍵的情況
        print(f"按下了 {key} 鍵")

def on_release(key):#鬆開按鍵時執行
    print(f"鬆開了 {key} 鍵")
    if key == pk.Key.esc:
        print("退出全局監聽")
        return False

class KBListener():
    def __init__(self):
        super(KBListener, self).__init__()
        # 通過屬性判斷按鍵類型。

    def start(self):
        with pk.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
