🔢 Number to Words (Indian Currency System)

A simple yet powerful Python program that converts any numerical value into words following the Indian numbering system — supporting Crores, Lakhs, Thousands, and more.

This logic might seem easy at first, but once you start building it, you’ll face multiple layers of exceptions and recursive challenges. It’s a perfect exercise to sharpen your logic-building skills in Python. 💡

🚀 Features

Converts numbers into readable Indian currency format (supports crores, lakhs, thousands, hundreds).

Handles special cases like “and” placement and multi-digit recursion correctly.

Clean, modular code using helper functions for readability and scalability.

Beginner-friendly logic that also tests your problem-solving and recursive thinking.

🧠 Tech Used

Python 3

🧩 Code Overview

two_digit(n): Converts numbers below 100 to words.

three_digit(n): Handles hundreds and “and” placements.

number_to_words(num): The main recursive function that breaks the number into crores, lakhs, thousands, and hundreds.

🧮 Example Output
Enter number: 12345678
one crore twenty three lakh forty five thousand six hundred and seventy eight

💬 Note

This project was created as part of a logic-building exercise in Python.
Try implementing the same logic in your preferred language — and see if you can make it even more optimal! ⚡


📦 Installation

Clone this repository and run it locally:
```bash
git clone https://github.com/<your-username>/Number-to-Words.git
cd Number-to-Words
python main.py

