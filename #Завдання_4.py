

#- пройтись по списку словників
#- витягти з кожного словника дату
#- конвертувати рядок дати в формат дати
#- витягнути поточну дату
#- порівняти дн з теперішньою датою.
#- тоді порахувати дні до наступного дн
#- якщо наступне дн попадає в проміжок 7 днів > занести словник у новий список. 
#- видрукувати новий список


from datetime import timedelta, datetime

def get_upcoming_birthdays(users)->list:
    lst=[]
    for i in users:
        bd=datetime.strptime(i.get("birthday"),"%Y.%m.%d").replace(year=2025).date()
        now=datetime.now().date()
        seven_day_window=now+timedelta(days=6)
            
        if bd>=now and bd<=seven_day_window:
                match bd.weekday():
                    case (5):
                     congratulation_date=bd+timedelta(days=2)
                    case (6):
                     congratulation_date=bd+timedelta(days=1)
                    case (_):
                     congratulation_date=bd
                    
                congratulation_date=congratulation_date.strftime("%Y.%m.%d")
        
                user_dictionary={"name":i["name"], "congratulation_date":congratulation_date}
                lst.append(user_dictionary) 
    return lst
                
users = [
    {"name": "John Doe", "birthday": "1990.10.29"},   # потрапляє в 7 днів
    {"name": "Jane Smith", "birthday": "1995.10.31"}, # потрапляє в 7 днів
    {"name": "Emily Johnson", "birthday": "1987.11.05"},
    {"name": "Michael Brown", "birthday": "1982.09.15"},
    {"name": "Olivia Davis", "birthday": "1998.07.22"},
    {"name": "Liam Wilson", "birthday": "1993.03.03"},
    {"name": "Sophia Taylor", "birthday": "1989.04.10"},
    {"name": "Noah Martinez", "birthday": "1991.12.20"},
    {"name": "Ava Anderson", "birthday": "1994.01.02"},
    {"name": "James Thomas", "birthday": "1992.05.25"}
]
                
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:")
for item in upcoming_birthdays:
   print(item)
       


        










#Критерії оцінювання:

#Актуальність та коректність визначення днів народження на 7 днів вперед.
#Правильність обробки випадків, коли дні народження припадають на вихідні.
#Читабельність та структурованість коду.


#Приклад:

#Припустимо, у вас є список users:



#Використання функції get_upcoming_birthdays:

#upcoming_birthdays = get_upcoming_birthdays(users)
#print("Список привітань на цьому тижні:", upcoming_birthdays)

#Якщо сьогодні 2024.01.22 результатом може бути:

#[
#    {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
#    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
#]

#Цей список містить інформацію про те, кого і коли потрібно привітати з днем народження.