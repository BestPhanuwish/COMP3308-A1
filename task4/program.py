def task4(algorithm, message_filename, dictionary_filename, threshold, letters, debug):
    
    with open(message_filename, 'r') as f:
        message = f.read()
        message_list = message.split()
        
    with open(dictionary_filename, 'r') as f:
        dict = f.read()
        dict_list = dict.split()
        dict_list = [x.lower() for x in dict_list] # nake sure that all the words in dict is in lowercase

    if algorithm == 'd':
        dfs()
    elif algorithm == 'b':
        bfs()
    elif algorithm == 'i':
        ids()
    elif algorithm == 'u':
        ucs()

    if debug == 'y':
        print("First few expanded states:")
    return ''

def dfs():

    return None

def bfs():
    return None

def ids():
    return None

def ucs():
    return None

def count_words(message_list, dict_list):
    count = 0
    for word in message_list:
        word = word.lower()
        ignore_char = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in ignore_char:
            word = word.replace(char, "")
        if word in dict_list:
            count += 1
    percentage = count/len(message_list) * 100
    return percentage

def nodelist(filename, letters):
    char_list = list(letters)
    pairs = swap(char_list)

    with open(filename, "r") as f:
        text = f.read()

    outputtxt = []
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
            outputtxt.append(newtext)
            messages += 1
    return messages, outputtxt

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


if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task4 function
    print(task4('d', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    print(task4('b', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    print(task4('i', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    