import math

def task5(message_filename, is_goal):
    #TODO
    if is_goal: # if it's goal node then return 0
        return 0
    
    # get message from file
    with open(message_filename, 'r') as f:
        message = f.read()
    
    # count frequency from each character
    alp_freq = {}
    for char in message:
        if char.upper() not in "AENOST":
            continue
          
        if char.upper() in alp_freq:
            alp_freq[char.upper()] += 1
        else:
            alp_freq[char.upper()] = 1
    
    # sorted alphabet based on frequency
    sorted_alp = sorted(alp_freq.keys(), key=lambda x: (-alp_freq[x], x))
    
    # initialise the theorically correct frequency
    key_ordering = "ETAONS"
    
    # count how many it doesn't match the key
    n = 0
    for i in range(len(sorted_alp)):
        if sorted_alp[i] != key_ordering[i]:
            n += 1
    
    return math.ceil(n/2)
          

if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task5 function
    print(task5('freq_eg1.txt', False))
    print(task5('freq_eg1.txt', True))
    print(task5('freq_eg2.txt', False))
