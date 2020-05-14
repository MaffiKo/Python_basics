user_answer = int(input("Введите секунды для расчёта: "))
hours = user_answer // 3600
minutes = (user_answer % 3600) // 60
sec = user_answer % 60
print(f"В заданном количесве секунд: {hours:02}:{minutes:02}:{sec:02}")