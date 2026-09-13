# 🎂 Birthday Wisher

A simple Python automation project that checks a birthday list and automatically sends a personalized birthday email when someone's birthday matches the current date.

## ✨ Features

- Reads birthday information from a CSV file.
- Checks if someone has a birthday today.
- Randomly selects one of several birthday letter templates.
- Personalizes the letter with the recipient's name.
- Sends the birthday email automatically.

## 🛠️ Technologies Used

- Python
- Pandas
- SMTP
- Gmail SMTP

## 📁 Project Structure

```text
Birthday Wisher/
│
├── main.py
├── birthdays.csv
└── letter_templates/
    ├── letter_1.txt
    ├── letter_2.txt
    └── letter_3.txt

```
## ✉️ Letter Templates

Birthday messages are stored as .txt files inside the letter_templates folder.

For example:
```
Dear [NAME],

Happy Birthday!

I hope you have an amazing day filled with happiness and joy.

Best wishes!
```

[NAME] is automatically replaced with the person's name from birthdays.csv.

## 🚀 How to Run Your Own
1. Clone the repository.
2. Install the required packages:
```pip install pandas```
3. Add your birthday information to birthdays.csv.
4. Add your birthday letter templates to the letter_templates folder.
5. Set your Gmail email and App Password as environment variables.
6. Run: ```python main.py```

The program will check whether anyone has a birthday today and send a personalized email if there is a match.

## 👩‍💻 Author

### Aashi Chatterjee

A simple Python automation project built as part of learning Python and working with APIs, files, data, and email automation.




