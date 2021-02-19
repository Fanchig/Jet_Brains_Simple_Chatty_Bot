A = int(input())  # Sleep at least that
B = int(input())  # Don't sleep more than that
H = int(input())  # What you sleep

if A <= H <= B:
    print("Normal")
elif H < A:
    print("Deficiency")
else:
    print("Excess")