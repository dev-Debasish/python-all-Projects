#   here we take 20 questions that meets the requirments of the money [levels]...
questions = [
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Who creats the SpeceX?", "Elon Musk", "Bill Gates", "Mark Jukerbark", "Ambani", 1],
    ["Which language has dictionary?", "python", "English", "javaScript", "php", 1],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
    ["Which language was used to creat fb?", "python", "English", "javaScript", "php", 4],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1280000, 2540000, 5080000, 10000000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(f"{question[0]}")
    print(f"a. {question[1]}      b. {question[2]} ")
    print(f"c. {question[3]}      d. {question[4]} ")

    reply = int(input("Enter your answer (1-4) or. 0 to quit: "))
    if reply == 0:
        if i == 0:
            break
        else:
            money = levels[i - 1]
            break
    if reply == question[-1]:
        print(f"correct answer, we have won Rs.{levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("Wrong Answer!!")
        break
    
print(f"Your take home money is {money}")




