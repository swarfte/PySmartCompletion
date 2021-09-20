import threading
import pynput as PP


class ListenerThread(threading.Thread):  # 創建用作監聽的線程
    def __init__(self):
        super().__init__()

    def run(self):
        pass


class KeyboardListener(object):
    def __init__(self):
        super().__init__()

