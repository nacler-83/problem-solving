import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


def unique_numbers(texts, calls):
    """
    Creates a list "collection" that has all outbound and inbound telephone
    numbers appended to it from the calls and texts dataset. Then prints the
    number of unique phone numbers in the collection.
    """
    d = {}
    for rows in texts:
        if rows[0] not in d:
            d[rows[0]] = 1
        if rows[1] not in d:
            d[rows[1]] = 1
    for rows in calls:
        if rows[0] not in d:
            d[rows[0]] = 1
        if rows[1] not in d:
            d[rows[1]] = 1
    count = len(d)
    result = f'There are {count} different telephone numbers in the records.'
    print(result)


unique_numbers(texts, calls)
