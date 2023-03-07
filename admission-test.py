#輸入 array，找出最大值
def find_max(numbers):
    #檢查輸入的 array 是否為空值
    if len(numbers) == 0:
        return None
    #檢查 array 中的元素是否為數字
    for number in numbers:
        if not isinstance(number, (int, float)):
            return None
    #找出最大值
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

#輸入 array，找出最目標值的位置
def find_position(numbers, target):
    #檢查輸入的 array 是否為空值
    if len(numbers) == 0:
        return None
    #找出目標值的位置    
    index = [i for i in range(len(numbers)) if numbers[i] == target]
    # 如果沒有找到目標值，返回 -1
    if not index:
        return -1
    return index
    
#返回一個值，該值顯示每個字符出現的次數
def count(input):
    char_count = {}
    for char in input:
        # 如果字元已經在字典中，增加計數
        if char in char_count:
            char_count[char] += 1
        # 如果字元還沒有在字典中，創建一個新的鍵值對
        else:
            char_count[char] = 1
    return char_count

#將相同 key 的 value 加總
def group_by_key(input):
    result = {}
    for item in input:
        key = item['key']
        value = item['value']
        # 如果鍵值已經在字典中，增加計數
        if key in result:
            result[key] += value
        # 如果鍵值還沒有在字典中，創建一個新的鍵值對
        else:
            result[key] = value
    return result

    
#What is Git and why is it used?
# Git 是一個分散式版本控制系統 (DVCS)，可幫助軟件開發團隊管理和跟踪他們代碼的變化。Git由Linus Torvalds在2005年創建，以管理Linux內核代碼而聞名。Git有多個優點，其中包括：
# 分散式：Git的分散式架構允許多個開發人員在同一時間對同一代碼庫進行獨立的更改，而不會干擾彼此的工作。
# 分支：Git支持輕鬆創建和合併分支，以便進行並行開發和實驗。
# 歷史追蹤：Git記錄每次提交的更改，使開發人員可以查看代碼庫的完整歷史，並查找特定更改的詳細信息。
# 集成：Git可以與其他工具和服務（如Jenkins，Travis CI和GitHub）集成，以構建，測試和部署代碼。
# 基本概念
# Git中的一些基本概念包括：
# 代碼庫：代碼庫是存儲代碼的地方。代碼庫可以是本地計算機上的目錄，也可以是在遠程服務器上的Git存儲庫。
# 提交：提交是將更改保存到代碼庫的過程。每次提交都有一個關聯的提交消息，用於描述更改的目的和內容。
# 分支：分支是指代碼庫的不同版本，通常用於並行開發和實驗。在創建分支時，Git將原始代碼庫複製一份，然後允許開發人員在副本中進行更改，而不會影響原始代碼庫。
# 合併：合併是將一個分支的更改合併到另一個分支的過程。當多個開發人員在不同的分支上進行工作時，合併是將他們的更改組合到一起的方法。



# What is the difference between List, Dictionary, Tuple and Set in Python?
# List（列表）：List 是一種有序、可變、可重複的資料類型，用方括號 [] 表示，可以存儲任何類型的資料。List 中的每個元素都有一個索引，可以透過索引來訪問和修改元素。

# Dictionary（字典）：Dictionary 是一種無序、可變、鍵值對映射的資料類型，用花括號 {} 表示，每個鍵值對之間用冒號 : 分隔，鍵和值之間用逗號 , 分隔。Dictionary 中的鍵必須是不可變的資料類型，如字符串、整數或元組，而值可以是任何資料類型。

# Tuple（元組）：Tuple 是一種有序、不可變、可重複的資料類型，用圓括號 () 表示，可以存儲任何類型的資料。Tuple 中的每個元素都有一個索引，可以透過索引來訪問元素，但是不能修改元素。

# Set（集合）：Set 是一種無序、可變、不可重複的資料類型，用花括號 {} 表示，每個元素之間用逗號 , 分隔。Set 只能存儲不可變的資料類型，如字符串、整數或元組，不能存儲可變的資料類型，如列表和字典。

# 總結來說，List、Dictionary、Tuple 和 Set 是四種不同的資料類型，每種類型都有其自己的特點和用途。List 適用於有序的、可變的資料集合，Dictionary 適用於鍵值對映射的資料集合，Tuple 適用於有序的、不可變的資料集合，Set 適用於無序、不可重複的資料集合。

   
    
    
    


    

