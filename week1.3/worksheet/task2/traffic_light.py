"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Alex Nicklin
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

# print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

position = 0
state_count = 1
while systime <= maxtime:
    if state_count <= states[state]:
        print(f"Time {systime:03} State {state}")

        systime += 1
        state_count += 1
    else:
        if systime % 15 == 0:
            position = 0
        else:
            position += 1
        state_count = 1
        state = list(states)[position]

# At the end of each step you should output the time and state using the statement on line 14