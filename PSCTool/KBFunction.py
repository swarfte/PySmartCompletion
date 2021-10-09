import json
import pynput.keyboard as pk
import re

def find_in_head():
    pass

def find_in_inside(vocabulary,data):
    sentence = "".join(vocabulary)
    choice = re.compile(f"{sentence}")
    match_word = []
    for x in range(len(data)):
        temp = re.search(choice,data[x])
        #print(str(temp))
        if str(temp) != "None" :
            match_word.append(data[x])
    return match_word

    # match_word = []
    # for x in range(len(vocabulary)):
    #     temp = []
    #     if x == 0:
    #         for y in range(len(data)):
    #             if vocabulary[x] in data[y] :
    #                 temp.append(data[y])
    #                 match_word.append(temp)
    #     else:
    #         for z in range(len(match_word[x-1])): #層層篩選
    #             if vocabulary[x] in match_word[x-1][z]:
    #                 temp.append(match_word[x-1][z])
    #                 match_word.append(temp)
    #
    # return match_word[len(match_word)-1] #翻回滿足全部篩選的生字

def open_json(path):
    with open (path,"r",encoding="utf-8") as f:
        data = json.load(f)
    return data

def completion(config,vocabulary):
    target = "WordBank_path"#指定讀取的數據庫
    vocabulary_type = "english_word" #指定讀取的生字
    data = open_json(open_json(config)[target])[vocabulary_type] #*獲取對應數據庫的全部英文生字
    #key_match = [x for x in data if str(last_key).replace("'","") in x[:1]]#去除多餘的單引號並匹配第一個生字
    print(find_in_inside(vocabulary, data))

def save_words_setup(key_input):
    if key_input:
        print("關閉 儲存生字功能")
        return False
    else:
        print("開啟 儲存生字功能")
        return True

def save_words(key,vocabulary):
    if key != pk.Key.ctrl_l and key != pk.Key.caps_lock:  # 無視左ctrl的操作和檢測操作人
        vocabulary.append(str(key).replace("'", ""))  # 去除多餘的單引號

def exitListen():
    print("退出全局監聽")
    return False  # 回傳false停止監聽

def current_words(vocabulary):
    print(vocabulary)
