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

if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task4 function
    print(task4('d', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    print(task4('b', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    print(task4('i', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    