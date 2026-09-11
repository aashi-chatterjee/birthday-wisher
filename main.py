import os
import datetime as dt
import pandas as pd
from random import randint
import smtplib

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

birthday_data = pd.read_csv("birthdays.csv").to_dict()

names = birthday_data["name"]
months = birthday_data["month"]
dates = birthday_data["day"]
email = birthday_data["email"]

current_date = dt.datetime.today().day
current_month = dt.datetime.today().month

# 2. Check if today matches a birthday in the birthdays.csv
for each_month in months:
    for each_date in dates:
        if current_date == dates[each_date] and current_month == months[each_month]:
            name = names[each_date]
            send_addr = email[each_date]

            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
            # with the person's actual name from birthdays.csv
            file_num = randint(1, 3)
            with open(f"letter_templates/letter_{file_num}.txt", "r+") as letter_file:
                letter_contents = letter_file.read()
                letter_contents = letter_contents.replace("[NAME]", name)
                print(letter_contents)

                # 4. Send the letter generated in step 3 to that person's email address.
                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs=send_addr,
                                        msg=f"Subject: HAPPY BIRTHDAY\n\n{letter_contents}"
                                        )
