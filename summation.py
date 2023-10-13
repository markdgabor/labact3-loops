# Coded by Mark Dunstan A. Gabor CITCS-1B
# DATE: October 12, 2023
C = 0
Process = 0
answer = int(input("Please type 4"))
while Process != 10:
    if answer != 4:
        print("Incorrect Response. Please type 4.")
        answer = int(input("Please type 4"))
    else:
        while C < 5:
            Process = Process + C
            C = C + 1
        else:
            print(Process)
