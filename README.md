#英文單詞補全

###程式示範:https://www.youtube.com/watch?v=Z3Vabk1IDag&ab_channel=SwarfteChau

###使用方法
* 第一步 開啟main.py(終端機提示模式) 或 main.exe(隱身模式)
* 第二步 按下**左ctrl**開啟輸入模式 開啟後會出現"$"提示字符
* 第三步 輸入任意數量的英文字
* 第四步 選擇匹配的模式
  * **4.A**  頭尾匹配模式
    * 輸入要搜索的生字的**頭尾**字母 按下**右shift**鍵進行匹配
  * **4.B** 由頭開始匹配模式
    * 依次輸入要搜索的生字的字母 輸入的字母越多越精準 
    * 按下**左shift**進行匹配
  * **4.C** 包含匹配模式
    * 輸入任意數量要搜索的生字包含的字母(不限順序) 
    * 先按下**左ctrl**關閉輸入模式 再按下**左shift**進行匹配
  * 進行匹配之後便會輸出對應**數字**表示成功匹配的單詞數量
* 第五步 按下**左alt鍵**開啟輸出模式 開啟後會出現"$"提示字符
* 第六步 按下鍵盤上**1~9**的按鍵 便出輸出對應匹配的生字
  * 如果按下的數字超過匹配的數字數量便會出現"$"提示字符
* 按下**esc**即時退出鍵盤監聽

###主要按鍵功能
* **左ctrl** : 開啟/關閉輸入模式
* **右ctrl** : 清空儲存的輸入生字
* **左Shift** : 
  * 開啟輸入模式時: 由頭開始匹配模式
  * 關閉輸入模式時: 包含匹配模式
* **右shift** : 頭尾匹配模式
* **左alt**: 開啟/關閉輸出模式
* **右alt** : (終端機)顯示目前儲存的生字

###數據庫配置
* 在**config**檔案夾中能加入額外的數據庫
* **WordBank1.json**為預設的數據庫
* 在**setting.json**中修改**WordBank_path**屬性能指定新的數據庫

###版本號:V1.1.4