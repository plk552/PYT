while True:
    num1 = int(input("введите первое число: "))
    num2 = int(input("введите второе число: "))
    
    operation = str(input("Выберите математическую операцию: '+' '-' '*' '/': "))
    if operation == '+':
        result =  num1 + num2
    elif operation == '-':
        result =  num1 - num2
    elif operation == '*':
        result =  num1 * num2
    elif operation == '/':
        result =  num1 / num2
    print(f'ответ: {result}')
    
    if 'y' == input("желаете ли вы завершить работу? y|n"):
        break