import json
import pynput.keyboard as pk
import re


def on_press_text(key):  # 顯示按下的鍵
    try:
        print(f"按下了 {key.char} 鍵")
    except AttributeError:  # 特殊按鍵的情況
        print(f"按下了 {key} 鍵")


def on_release_text(key):  # 顯示放開的鍵
    print(f"鬆開了 {key} 鍵")


def find_in_head(vocabulary, data):  # 由頭開始搜索
    sentence = "".join(vocabulary)
    print(f"字符 {sentence} 啟用首字母匹配模式")
    choice = re.compile(f"^{sentence}")
    match_word = []
    for x in range(len(data)):
        temp = re.search(choice, data[x])
        if str(temp) != "None":
            match_word.append(data[x])
    return match_word


def find_in_inside(vocabulary, data):  # 搜索是否包含在內
    sentence = "".join(vocabulary)
    print(f"字符 {sentence} 啟用包含字母匹配模式")
    match_word = []
    for x in range(len(vocabulary)):
        temp = []
        if x == 0:
            for y in range(len(data)):
                if vocabulary[x] in data[y]:
                    temp.append(data[y])
                    match_word.append(temp)
        else:
            for z in range(len(match_word[x - 1])):  # 層層篩選
                if vocabulary[x] in match_word[x - 1][z]:
                    temp.append(match_word[x - 1][z])
                    match_word.append(temp)

    return match_word[len(match_word) - 1]  # 回傳包含全部篩選生字的單詞


def find_in_head_and_tail(config, vocabulary):  # 查找頭尾匹配的生字
    sentence = "".join(vocabulary)
    print(f"字符 {sentence} 啟用頭尾字母匹配模式")
    data = get_word_list(config, vocabulary)
    choice = re.compile(f"^{vocabulary[0]}[a-z]*{vocabulary[1]}$")
    match_word = []
    for x in range(len(data)):
        temp = re.search(choice, data[x])
        if str(temp) != "None":
            match_word.append(data[x])

    print(match_word)
    return match_word


def open_json(path):  # 加載設定檔
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def key_word_match(config, vocabulary, begin):  # 多生字匹配模式
    data = get_word_list(config, vocabulary)
    if begin:  # 判斷是首字母匹配還是包含匹配模式
        match_word = find_in_head(vocabulary, data)
    else:
        match_word = find_in_inside(vocabulary, data)

    print(match_word)

    return match_word


def get_word_list(config, vocabulary):  # 獲取數據庫的生字
    key_match = "".join(vocabulary)
    target = "WordBank_path"  # 指定讀取的數據庫
    vocabulary_type = "english_word"  # 指定讀取的生字
    data = open_json(open_json(config)[target])[vocabulary_type]  # *獲取對應數據庫的全部英文生字

    return data


def save_words_setup(key_input):  # 儲存生字功能
    if key_input:
        print("關閉 儲存生字功能")
        return False
    else:
        print("開啟 儲存生字功能")
        return True


def save_words(key, vocabulary):  # 判斷生字
    if key != pk.Key.ctrl_l and key != pk.Key.ctrl_r:  # 無視左右ctrl的開關操作和消除生字操作
        if key != pk.Key.shift_l and key != pk.Key.shift_r:  # 無視左右shirt的搜索功能
            if key != pk.Key.alt_l and key != pk.Key.alt_gr:  # 無視左右alt的輸出和視檢測生字操作
                vocabulary.append(str(key).replace("'", ""))  # 去除多餘的單引號


def clean_save_word(vocabulary):  # 清空保留的生字
    print('清空儲存的生字')
    vocabulary = []
    return vocabulary


def exit_listen():  # 退出監聽
    print("退出全局監聽")
    return False  # 回傳false停止監聽


def current_words(vocabulary):  # 顯示當前的生字
    print(vocabulary)


def output_match_word_number(match_word, keyboard):
    number = str(len(match_word))
    print(f"一共有 {number} 個生字滿足條件")
    for x in range(len(number)):
        keyboard.press(number[x])  # down keyboard
        keyboard.release(number[x])  # up keyboard

    return number


def output_choice_match_word(key, match_word, keyboard):  # 輸出被選擇的匹配生字
    number = int(str(key)[1:-1]) - 1
    output_word = match_word[number]
    print(f"選擇的生字為 {output_word} ")
    for x in range(len(output_word)):
        keyboard.press(output_word[x])
        keyboard.release(output_word[x])
