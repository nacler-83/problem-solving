import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order
with no duplicates.
"""


def valid_numbers(calls, texts):
    d = {}
    """
    Start by building a dictionary that has all the valid phone numbers,
    defined as any sending or receiving a text, or any receiving a phone call.
    """
    for rows in texts:
        if rows[0] not in d:
            d[rows[0]] = 1
        else:
            d[rows[0]] += 1

        if rows[1] not in d:
            d[rows[1]] = 1
        else:
            d[rows[1]] += 1

    for rows in calls:
        if rows[1] not in d:
            d[rows[1]] = 1
        else:
            d[rows[1]] += 1

    return d


def find_telemarketers(calls, texts):
    d = {}
    valid_list = valid_numbers(calls, texts)
    """
    Compare the list of outbound calls to the valid list, and build a
    dictionary with those numbers not found in valid list.
    """
    print("These numbers could be telemarketers:")

    for rows in calls:
        if rows[0] not in valid_list:
            d[rows[0]] = 1

    for i in sorted(d):
        print(i)


find_telemarketers(calls, texts)
