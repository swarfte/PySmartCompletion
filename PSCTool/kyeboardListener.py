import threading
import pynput as PP

class ListenerThread(threading.Thread):  # 創建用作監聽的線程
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def run(self):
        print("正在全局監聽")
        KeyboardListener().listen()

    def stop(self):
        #print("退出全局監聽")
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

class KeyboardListener(object):#用作監聽全局按鈕
    def __init__(self):
        super().__init__()

    def listen(self):

        def keyboard_down(key):
            print(str(key) + "鍵被按下")


        def keyboard_up(key):
            print(str(key) + "鍵被放開")


        def check_keyboard(check,key):#用作檢測按鍵是否被按下
            use_key = str(key)
            if key == PP.keyboard.KeyCode(char= use_key) or key == PP.keyboard.KeyCode(char = use_key.upper()):
                check = True


        with PP.keyboard.Listener(on_press = keyboard_down , on_release = keyboard_up) as listener:
            listener.join()

if __name__ == "__main__":
    listener = ListenerThread()
    listener.start()