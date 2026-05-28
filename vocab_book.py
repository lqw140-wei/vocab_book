import json
import random

DATA_FILE = "vocab_data.json"
def load_words():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            words = json.load(file)
        print("已加载", len(words), "个单词。")
        return words
    except FileNotFoundError:
        print("未找到数据文件，已创建新的单词本。")
        return []
    except json.JSONDecodeError:
        print("数据文件损坏，已创建新的单词本。")
        return []
def save_words(words):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(words, file, indent=2, ensure_ascii=False)

words = load_words()
while True:
    print("\n===== 个人单词本 =====")
    print("1. 添加单词")
    print("2. 查看所有单词")
    print("3. 随机测验")
    print("4. 删除单词")
    print("5. 退出系统")
    print("===================")

    choice_str = input("请输入你的选择（1-5）")
    try:
        choice = int(choice_str)
    except ValueError:
        print("请输入数字！")
        continue
    if choice == 1:
        english = input("请输入英文单词：")
        chinese = input("请输入中文释义：")
        word = {"英文": english, "中文": chinese}
        words.append(word)
        save_words(words)
        print("单词", english, "-",chinese, "已添加！")
    #功能2：查看所有单词
    elif choice == 2:
        if len (words) == 0:
            print("目前没有单词，快去添加吧。")
        else:
            print("所有单词如下：")

            for i in range(len(words)):
                w = words[i]
                eng = w["英文"]
                chn = w["中文"]
                print(i,". ", eng, " - ", chn)
    elif choice == 3:
        if len(words) == 0:
            print("目前没有单词，无法测验。")
        else:
            quiz_word = random.choice(words)
            chinese_question = quiz_word["中文"]
            correct_answer = quiz_word["英文"]
            print("请写出以下中文对应的英文单词：")
            print("题目：",chinese_question)
            user_answer = input("你的答案：")
            if user_answer.strip().lower() == correct_answer.strip().lower():
                print("回答正确！太棒了！")
            else:
                print("回答错误。正确答案是：", correct_answer)


    elif choice == 4:
        if len(words) == 0:
            print("目前没有单词，无法删除。")
        else:
            print("当前单词列表：")
            for i in range(len(words)):
                w = words[i]
                print(i, ".", w["英文"], " - ", w["中文"])
            index_str = input("请输入要删除的单词编号：")
            try:
                index = int(index_str)
            except ValueError:
                print("请输入有效的数字编号！")
                continue

            if index >= 0 and index < len(words):
                removed = words.pop(index)
                save_words(words)
                print("已删除单词：", removed["英文"], " - ", removed["中文"])
            else:
                print("无效编号，请重新操作。")
    elif choice == 5:
        print("退出系统，再见！")
        break
    else:
        print("无效选择，请输入1-5之间的数字。")



