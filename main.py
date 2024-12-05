num = list(map(int,input("введите цифры: ").split())) #ввод числа и перекидывание его в список
spisok = [numbers ** 2 for numbers in num] # создание списка с квадратами чисел
print(spisok) #вывод
