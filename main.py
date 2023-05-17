import random
import smtplib
from datetime import datetime
import pandas

today = datetime.now()
today_tuple = (today.month, today.day)
MY_EMAIL = "abcd@gmail.com"
MY_PASSWORD = "aveoafneuian13431**"

# Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


