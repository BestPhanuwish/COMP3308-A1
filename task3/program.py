def task3(message_filename, dictionary_filename, threshold):
    
    with open(message_filename, 'r') as f:
        message = f.read()
        message_list = message.split()
        
    with open(dictionary_filename, 'r') as f:
        dict = f.read()
        dict_list = dict.split()
        dict_list = [x.lower() for x in dict_list] # nake sure that all the words in dict is in lowercase
    
    # counting every matched words from message
    count = 0
    for word in message_list:
        
        # clean the word in message
        word = word.lower()
        ignore_char = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in ignore_char:
            word = word.replace(char, "")
        
        if word in dict_list:
            count += 1
    percentage = count/len(message_list) * 100
    
    return_message = ""
    if percentage >= threshold:
        return_message = "True\n{:.2f}".format(percentage)
    else:
        return_message = "False\n{:.2f}".format(percentage)
    
    return return_message

if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task3 function
    print(task3('jingle_bells.txt', 'dict_xmas.txt', 90))
    print(task3('fruit_ode.txt', 'dict_fruit.txt', 80))
    print(task3('amazing_poetry.txt', 'common_words.txt', 95))
    