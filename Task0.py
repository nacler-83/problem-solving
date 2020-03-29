import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number>
at time <time>"
"Last record of calls, <incoming number> calls <answering number> at
time <time>, lasting <during> seconds"
"""


def first_text(data):
    """
    Prints semantically the first record within the texts dataset.
    """
    incoming_number = data[0][0]
    answering_number = data[0][1]
    time = texts[0][2]
    result = f'First record of texts, {incoming_number} texts {answering_number} at time {time}'
    print(result)


def last_call(data):
    """
    Prints semantically the last record within the calls dataset.
    """
    total = len(data) - 1
    incoming_number = data[total][0]
    answering_number = data[total][1]
    time = data[total][2]
    duration = data[total][3]
    result = f'Last record of calls, {incoming_number} calls {answering_number} at time {time}, lasting {duration} seconds'
    print(result)


first_text(texts)
last_call(calls)
