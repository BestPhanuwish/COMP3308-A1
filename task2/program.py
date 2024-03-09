def task2(filename, letters):
    char_list = list(letters)
    pairs = swap(char_list)

    with open(filename, "r") as f:
        text = f.read()

    outputtxt = ""
    messages = 0
    for pair in pairs:
        newtext = ""
        n = 0
        for char in text:
            if char.lower() == pair[0].lower():
                if char.isupper():
                    newtext += pair[1]
                else:
                    newtext += pair[1].lower()
            elif char.lower() == pair[1].lower():
                if char.isupper():
                    newtext += pair[0]
                else:
                    newtext += pair[0].lower()
            else:
                newtext += char
                n += 1
        if n != len(text):
            outputtxt += newtext + "\n" + "\n"
            messages += 1
    outputtxt = str(messages) + "\n" + outputtxt
    return outputtxt.rstrip()


def swap(char_list):
    pairs = []
    char_list.sort()
    for i in range(len(char_list)):
        for j in range(i + 1, len(char_list)):
            if char_list[i] == char_list[j]:
                continue
            pair = [char_list[i], char_list[j]]
            pairs.append(pair)
    return pairs


if __name__ == "__main__":
    # Example function calls below, you can add your own to test the task2 function
    print(task2("spain.txt", "ABE"))
    print(task2("ai.txt", "XZ"))
    print(task2("ai.txt", "AA"))
    print(task2("cabs.txt", "ABZD"))
