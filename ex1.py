from datetime import datetime

def get_days_from_today(date: str)->int:
    try:
        input_date =datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return f"🙈 You've entered not acceptable date: {date}. Expected YYYY-MM-DD"
    except Exception as e:
        return f"🫠 Oops, something is wrong.return"
    else:    
        now = datetime.now()
        difference_in_days=input_date.toordinal()-now.toordinal()
        return difference_in_days
    
date=input("Enter date YYYY-MM-DD:")
result=get_days_from_today(date)

if isinstance(result, str):
    print(result)
else:
    print(f"Difference in days: {result}🤌")

 # як вам емоджі?)))))
 