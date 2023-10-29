# TODO  Напишите функцию count_letters
def count_letters(main_str):
    result={}
    main_str=main_str.lower()
    for i in main_str:
        if i.isalpha():
            if i in result:
                result[i]+=1
            else:
                result[i]=1
    return result
# TODO Напишите функцию calculate_frequency
def calculate_frequency(dic_letters):
    result = {}
    total=sum(dic_letters.values())
    for key,value in dic_letters.items():
        result[key]=value/total
    return result


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
dic_letters=count_letters(main_str)
dic_frequency=calculate_frequency(dic_letters)

for key,value in dic_frequency.items():
    print(f"{key}: {value:.2f}")

# TODO Распечатайте в столбик букву и её частоту в тексте
