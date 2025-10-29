from datetime import datetime

def get_days_from_today(date: str)->int:
    try:
        input_date =datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(f"You've entered not acceptable date: {date}")
    except SystemError:
        print(f"Please enter a date. in format: YYYY-MM-DD")
    except Exception as e:
        print("Oops, something is wrong. ")
    else:    
        
     now = datetime.now()

     difference_in_days=now.toordinal()-input_date.toordinal()
    return difference_in_days
    
date=input("Enter date YYYY-MM-DD:")
print(get_days_from_today(date))




 #завдання. При коректних даних працює правильно. 
 #Але не виконується умова ТЗ "Обробка винятків: функція має впоратися з неправильним форматом вхідних даних." 
 #Тобто якщо у функцію зайде, наприклад, "13.14.2000", то функція не повинна викликати помилку,
 #а коректно її обробити — наприклад, повідомити про помилку, повернути None, або видати зрозуміле повідомлення.