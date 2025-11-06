# Number to words in Indian currency system (supports crores, lakhs, thousands)
#Author : Akshith Kendyala

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
        "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def two_digit(n):
    if n < 20:
        return ones[n]
    else:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")

def three_digit(n):
    result = ""
    if n > 99:
        result += ones[n // 100] + " hundred"
        n = n % 100
        if n:
            result += " and "
    if n > 0:
        result += two_digit(n)
    return result

def number_to_words(num):
    if num == 0:
        return "zero"
    
    result = ""
    
    crore = num // 10000000
    num = num % 10000000
    if crore:
        result += number_to_words(crore) + " crore "
    
    lakh = num // 100000
    num = num % 100000
    if lakh:
        result += number_to_words(lakh) + " lakh "
    
    thousand = num // 1000
    num = num % 1000
    if thousand:
        result += number_to_words(thousand) + " thousand "
    
    if num > 0:
        result += three_digit(num)
    
    return result.strip()

num = int(input("Enter number: "))
res = number_to_words(num)
print(res)
