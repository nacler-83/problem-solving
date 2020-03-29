import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on
the phone during September 2016.".
"""


def longest_time_on_phone(data):
    """
    Prints the phone number that spent the most amount of time on the phone
    in the calls dataset, as well as the duration of time on the phone.
    """
    d = {}
    for rows in data:
        if rows[0] in d:
            d[rows[0]] = d.get(rows[0]) + int(rows[3])
        else:
            d[rows[0]] = int(rows[3])

        if rows[1] in d:
            d[rows[1]] = d.get(rows[1]) + int(rows[3])
        else:
            d[rows[1]] = int(rows[3])

    number = max(d, key=d.get)
    duration = d.get(number)

    result = f"{number} spent the longest time, {duration} seconds, on the phone during September 2016."
    print(result)


longest_time_on_phone(calls)
