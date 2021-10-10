import pynput.keyboard as pk
import PSCTool.KBFunction as PF

# 鍵盤監聽全局變量
config = None
vocabulary = []
key_input = False


def load_json(setting):  # 讀取設定檔用
    global config
    config = setting


def key_down(key):  # 按下按鍵時執行
    PF.on_press_text(key)  # 輸出文本


def key_up(key):  # 鬆開按鍵時執行
    global config  # 設定檔
    global vocabulary  # 待查詢的生字
    global key_input  # 儲存生字的開關

    PF.on_release_text(key)  # 輸出文本

    # 設置退出監聽優先級最高
    if key == pk.Key.esc:  # 退出監聽
        return PF.exit_listen()

    if key == pk.Key.ctrl_l:  # *啟動/關閉儲存生字的功能
        key_input = PF.save_words_setup(key_input)

    if key == pk.Key.alt_l:  # 顯示目前的生字
        PF.current_words(vocabulary)

    if key_input:  # 啟用時儲存生字
        PF.save_words(key, vocabulary)

    if key == pk.Key.alt_r:  # *清空儲存的生字
        vocabulary = PF.clean_save_word(vocabulary)

    if key == pk.Key.shift_l:  # 按生字搜索功能
        if len(vocabulary) > 0:
            PF.key_word_match(config, vocabulary, key_input)  # True為啟動首字母匹配功能,False為啟動包含搜索

    if key == pk.Key.shift_r:  # 啟動頭尾字母匹配模式
        if len(vocabulary) == 2:
            PF.find_in_head_and_tail(config, vocabulary)


class KBListener:  # 用於監聽鍵盤線程
    def __init__(self, config):
        super(KBListener, self).__init__()
        load_json(config)

    def start(self):  # 啟動線程
        with pk.Listener(on_press=key_down, on_release=key_up) as listener:
            listener.join()
