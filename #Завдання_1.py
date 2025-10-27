
from datetime import datetime

def get_days_from_today(date: str)->int:
    input_date =datetime.strptime(date, "%Y-%m-%d")
    now = datetime.now()

    difference_in_days=now.toordinal()-input_date.toordinal()
    return difference_in_days
    
date=input("Enter date YYYY-MM-DD:")
print(get_days_from_today(date))


