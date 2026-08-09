def testing(answer:str):
    parts = answer.split("#")
    print(parts[0])
    if input() == parts[1]:
        return 1
    return 0

def print_result(correct_answers):
    #Подсчёт
    if correct_answers <= 2:
        print('На данный момент мы не готовы рассмотреть Вас как потенциального кандидата на должность.')
    elif correct_answers == 3:
        print('Пройдите дополнительную подготовку и возращайтесь снова!')
    elif correct_answers >= 4:
        print('Вы прошли тестирование! Ждём Вас на следующем этапе собеседования!')