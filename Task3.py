import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with
no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def unique_area_codes(data):
    d = defaultdict(int)
    """
    Function to find and count all unique area codes being called by people
    in Bangalore. We will use a default dictionary as our holder.
    """
    for rows in data:
        """
        Our input data has outbound number at index 0. We are only concerned
        with people calling from Bangalore which is areacode (080).
        """
        if (rows[0][:5] == '(080)'):
            """
            Our input data has receiving number at index 1. Mobile numbers
            start with 7, 8 or 9 with four digits areacodes. Landline
            numbers start with '(' have their areacode encapsulated by
            paranthesis. Telemarketers numbers start with 140 which is
            their areacode.
            """
            if (rows[1][:1] == '7' or rows[1][:1] == '8' or rows[1][:1] == '9'):
                areacode = rows[1][:4]
                if areacode not in d:
                    d[areacode] = 1
                else:
                    d[areacode] += 1
            elif (rows[1][:1] == '('):
                opening = '('
                closing = ')'
                areacode = rows[1][rows[1].find(opening)+len(opening):rows[1].rfind(closing)]
                if areacode not in d:
                    d[areacode] = 1
                else:
                    d[areacode] += 1
            elif (rows[1][:3] == '140'):
                areacode = '140'
                if areacode not in d:
                    d[areacode] = 1
                else:
                    d[areacode] += 1

    return d


def local_call_percentage(data):
    areacodes = unique_area_codes(data)
    local_calls = areacodes['080']
    total_calls = 0
    """
    We want to print out all the unique area codes as well as calculate a
    percentage of calls make to 080 (local) vs total calls to all areacodes.
    """
    print("The numbers called by people in Bangalore have codes:")

    for i in sorted(areacodes):
        print(i)
        total_calls += areacodes[i]

    percentage = round((local_calls / total_calls) * 100, 2)

    print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


local_call_percentage(calls)
