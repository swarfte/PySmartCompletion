import pynput.keyboard as pk
import PSCTool.KBFunction as PF

# 鍵盤監聽使用的全局變量
config = None
input_vocabulary = []
key_input = False
key_output = False
match_word = []
keyboard = pk.Controller()
tip_symbol = "$"
tip_str = False


def load_json(setting):  # 讀取設定檔用
    global config
    config = setting


def key_down(key):  # 按下按鍵時執行
    PF.on_press_text(key)  # 輸出文本


def key_up(key):  # 鬆開按鍵時執行
    global config  # 設定檔
    global input_vocabulary  # 待查詢的生字
    global key_input  # 儲存生字的開關
    global key_output  # 輸出生字的開關
    global keyboard  # 虛擬鍵盤
    global match_word  # 儲存匹配的生字
    global tip_symbol  # 用於模式切換的提示
    global tip_str  # 判斷當前的文字是否為提示字符

    PF.on_release_text(key)  # 輸出文本

    # 設置退出監聽優先級最高
    if key == pk.Key.esc:  # 退出監聽
        return PF.exit_listen()

    if key_input:  # 啟用時儲存生字
        # tip_str = PF.auto_delete_tip_str(keyboard, tip_str)
        PF.save_words(key, input_vocabulary, tip_symbol)

    if key == pk.Key.ctrl_l:  # *啟動/關閉儲存生字的功能
        tip_str = PF.save_words_setup_tip(key_input, keyboard, tip_symbol, tip_str)  # 提示功能
        key_input = PF.save_words_setup(key_input)

    if key == pk.Key.alt_gr:  # 顯示目前的生字 (調試用)
        PF.current_words(input_vocabulary)

    if key == pk.Key.ctrl_r:  # *清空儲存的生字
        tip_str = PF.clean_word_tip(keyboard, tip_symbol, tip_str)
        input_vocabulary, key_input, key_output = PF.clean_word(input_vocabulary)  # 同時關閉輸入和輸出狀態

    if key == pk.Key.shift_l:  # 按生字搜索功能
        if len(input_vocabulary) > 0:
            match_word = PF.key_word_match(config, input_vocabulary, key_input)  # True為啟動首字母匹配功能,False為啟動包含搜索
            key_input = False
            PF.output_match_word_number(match_word, keyboard)  # 在模擬鍵盤輸入有多少個生字匹現

    if key == pk.Key.shift_r:  # 啟動頭尾字母匹配模式
        if len(input_vocabulary) == 2:
            match_word = PF.find_in_head_and_tail(config, input_vocabulary)
            key_input = False
            PF.output_match_word_number(match_word, keyboard)

    if key == pk.Key.alt_l:  # 用於選擇和輸出匹配的生字
        tip_str = PF.output_mode_setup_tip(key_output, keyboard, tip_symbol, tip_str)
        key_output = PF.output_mode_setup(key_output)

    if key_output:  # 啟用時輸出被選擇的匹配生字
        if str(key)[1:-1].isdigit() and len(match_word) != 0:
            try:
                PF.output_choice_match_word(key, match_word, keyboard)
            except Exception as ex:
                PF.output_error(keyboard, tip_symbol, ex)


class KBListener:  # 用於監聽鍵盤線程
    def __init__(self, config):
        super(KBListener, self).__init__()
        load_json(config)

    def start(self):  # 啟動線程
        with pk.Listener(on_press=key_down, on_release=key_up) as listener:
            listener.join()
