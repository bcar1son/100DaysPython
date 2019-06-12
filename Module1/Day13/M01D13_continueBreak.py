"""
    Author:         Ben Carlson
    Project:        100DaysPython
    File:           M01D13_continueBreak.py
    Creation Date:  2019-06-12
    Description:    Continue Break.
"""

motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed " \
             "Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! " \
             "Who's with me? Let's go!"
output = ""
for letter in motivation:
    if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
        output += letter
print(output)

output = ""
for letter in motivation:
    if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
        continue
    else:
        output += letter
print(output)

output = ""
for letter in motivation:
    if letter.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        output += letter
    else:
        break
print(output)
