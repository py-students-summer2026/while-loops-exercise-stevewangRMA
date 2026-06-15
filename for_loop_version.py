def get_starting_number():
    while True:
        response = input("How many bottles of beer on the wall? ")
        if response.isnumeric():
            number = int(response)
            if number >= 1:
                return number


def sing(start):
    for n in range(start, 0, -1):
        if n == 1:
            current = "1 bottle"
        else:
            current = str(n) + " bottles"

        print(current + " of beer on the wall, " + current + " of beer.")

        remaining = n - 1
        if remaining == 0:
            remaining_phrase = "no more bottles"
        elif remaining == 1:
            remaining_phrase = "1 bottle"
        else:
            remaining_phrase = str(remaining) + " bottles"

        if n == 1:
            print("Take it down, pass it around, " + remaining_phrase + " of beer on the wall!")
        else:
            print("Take one down, pass it around, " + remaining_phrase + " of beer on the wall.")

        if n > 1:
            print()