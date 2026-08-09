#Код Бабошина Максима
def testing(question):
    parts = question.split("#")
    print(parts[0])
    if input() == parts[1]:
        return 1
    return 0

def get_result(correct_answers):
    #Подсчёт
    if correct_answers <= 2:
        return 'На данный момент мы не готовы рассмотреть Вас как потенциального кандидата на должность.'
    if correct_answers == 3:
        return 'Пройдите дополнительную подготовку и возращайтесь снова!'
    return 'Вы прошли тестирование! Ждём Вас на следующем этапе собеседования!'
