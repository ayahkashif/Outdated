#format output to YYYY-MM-DD
#input --> september 8, 1636 or 9/8/1636
#no more than 31 days per month

list = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

while True:
    date = input("Date: ")
    if "/" in date:
        month, date, year = date.split("/")
        if month.isdigit() and date.isdigit() and 1 <= int(month) <= 12 and 1 <= int(date) <= 31:
            break
        elif month.isdigit() == False and year.isdigit() == False:
            alpha = []
            digit = []
            for _ in month:
                if _.isdigit():
                    digit.append(_)
                else:
                    alpha.append(_)
            month = digit[0]
            alpha2 = []
            digit2 = []
            for _ in year:
                if _.isdigit():
                    digit2.append(_)
                else:
                    alpha2.append(_)
            a = digit2[0]
            b = digit2[1]
            c = digit2[2]
            d = digit2[3]
            year = a + b + c + d
            break
        else:
            continue
    elif "," in date:
        first, year = date.split(", ")
        month, date = first.split(" ")
        month = month.title()
        try:
            list[month]
        except KeyError:
            pass
        else:
            month = list[month]
            if 1 <= int(date) <= 31:
                break
            else:
                continue

year = int(year)
month = int(month)
date = int(date)

print(f"{year}-{month:02}-{date:02}")

