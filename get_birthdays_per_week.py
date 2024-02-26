from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    birthday_next_week_dict = {}
    today = datetime.today().date()
    
    for user in users:
        birthdayConverted = user["birthday"].date()
        birthday_this_year = birthdayConverted.replace(year=today.year)

        # is the birthday this or nex year
        if birthday_this_year < today:
            birthday_next_year = birthdayConverted.replace(year=today.year + 1)
            delta_days = (birthday_next_year - today).days
        else:
            delta_days = (birthday_this_year - today).days

        birthday_weekday = birthday_this_year.weekday()  

        # find who will have the birthday in the next 7 days
        if delta_days < 7: 
            if birthday_weekday >= 5:
                days = 7 - birthday_weekday
                birthday_this_year += timedelta(days=days)
            
            birthday_weekday_str = birthday_this_year.strftime("%A")
            
            # add persons to dict
            if birthday_weekday_str not in birthday_next_week_dict:
                birthday_next_week_dict[birthday_weekday_str] = [user['name']]
            else:
                birthday_next_week_dict[birthday_weekday_str].append(user['name'])

    # output persons who will have birthday in the next 7 days
    for day, names in birthday_next_week_dict.items():
        names_str = ", ".join(names)
        print(f"{day}: {names_str}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "John Doe", "birthday": datetime(1955, 2, 28)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 28)},
    {"name": "Steve Jobs II", "birthday": datetime(1955, 2, 25)},
    {"name": "Elon Musk", "birthday": datetime(1971, 6, 28)}
]

get_birthdays_per_week(users)
