import math

def task6(algorithm, message_filename, dictionary_filename, threshold, letters, debug):
    
    with open(message_filename, 'r') as f:
        message = f.read()
        
    with open(dictionary_filename, 'r') as f:
        dict = f.read()
        dict_list = dict.split()
        dict_list = [x.lower() for x in dict_list] # nake sure that all the words in dict is in lowercase

    first_child = generate_child(letters)
    expanded_10_message = []
    output = ""

    if algorithm == 'd':
        output, expanded_10_message = dfs(message, dict_list, threshold, first_child)
    elif algorithm == 'b':
        output, expanded_10_message = bfs(message, dict_list, threshold, first_child)
    elif algorithm == 'i':
        ids()
    elif algorithm == 'u':
        ucs()
    elif algorithm == 'g':
        output, expanded_10_message = greedy(message, dict_list, threshold, first_child)
    elif algorithm == 'a':
        a_star()

    if debug == 'y':
        output += "First few expanded states:\n"
        output += '\n\n'.join(expanded_10_message)
    return output

def dfs(message, dict_list, threshold, original_childs):
    # initialise output
    expanded_10_message = []
    key = ""
    solution = ""
    path_cost = 0
    max_fringe_size = 0
    output = ""
    
    # initialise global variable
    num_node_expanded = 0
    max_depth = 0
    fringe = [Node([])]
    
    while True:
        # get the first element on the list and delete it
        num_node_expanded += 1
        node = fringe.pop(0)
        max_depth = max(max_depth, node.depth)
        
        # perform the swap on current node
        test_message = swap(message, node.get_pairs())
        if num_node_expanded <= 10: # the first 10 expanded node will be remember to memory
            expanded_10_message.append(test_message)
        
        # check if the message is threshold% in dictionary
        percent = count_words(message.split(), dict_list)
        if percent >= threshold:
            key = node_to_key(node.get_pairs())
            solution = test_message
            path_cost = node.depth
            break
        
        # append the new node to the fringe (DFS we added it on the front)
        for child in reversed(original_childs): #DFS we need reverse the list so that left most node end up at the front of the list
            new_node = Node(node.get_pairs() + [child])
            fringe.insert(0, new_node)
        max_fringe_size = max(max_fringe_size, len(fringe))
        
        # break the loop if expanded more than 1000 node
        if num_node_expanded >= 1000:
            break
    
    # gathering output text
    output += print_solution(solution, key, path_cost)
    output += f"Num nodes expanded: {num_node_expanded}\n"
    output += f"Max fringe size: {max_fringe_size}\n"
    output += f"Max depth: {max_depth}\n"
    output += "\n"
        
    return output, expanded_10_message

def bfs(message, dict_list, threshold, original_childs):
    # initialise output
    expanded_10_message = []
    key = ""
    solution = ""
    path_cost = 0
    max_fringe_size = 0
    output = ""
    
    # initialise global variable
    num_node_expanded = 0
    max_depth = 0
    fringe = [Node([])]
    
    while True:
        # get the first element on the list and delete it
        num_node_expanded += 1
        node = fringe.pop(0)
        max_depth = max(max_depth, node.depth)
        
        # perform the swap message on current node
        test_message = swap(message, node.get_pairs())
        if num_node_expanded <= 10: # the first 10 expanded node will be remember to memory
            expanded_10_message.append(test_message)
        
        # check if the message is threshold% in dictionary
        percent = count_words(test_message.split(), dict_list)
        if percent >= threshold:
            key = node_to_key(node.get_pairs())
            solution = test_message
            path_cost = node.depth
            break
        
        # append the new node to the fringe (BFS we added it on the end)
        for child in original_childs:
            new_node = Node(node.get_pairs() + [child])
            fringe.append(new_node)
        max_fringe_size = max(max_fringe_size, len(fringe))
        
        # break the loop if expanded more than 1000 node
        if num_node_expanded >= 1000:
            break
    
    # gathering output text
    output += print_solution(solution, key, path_cost)
    output += f"Num nodes expanded: {num_node_expanded}\n"
    output += f"Max fringe size: {max_fringe_size}\n"
    output += f"Max depth: {max_depth}\n"
    output += "\n"
        
    return output, expanded_10_message

def ids():
    return None

def ucs():
    return None

def greedy(message, dict_list, threshold, original_childs):
    # initialise output
    expanded_10_message = []
    key = ""
    solution = ""
    path_cost = 0
    max_fringe_size = 0
    output = ""
    
    # calculate original alphabet frequency from message
    GOAL_KEY_ORDERING = "ETAONS"
    ORIGINAL_FREQ = generate_key_frequency(message, "AENOST")
    h = count_match_freq(ORIGINAL_FREQ, GOAL_KEY_ORDERING)
    
    # initialise independent global variable
    num_node_expanded = 0
    max_depth = 0
    fringe = [Node([], h)] # this starter node is the root node where h is original frequency compare to goal frequency
            
    while True:
        # get the first element on the list and delete it
        num_node_expanded += 1
        node = fringe.pop(0)
        max_depth = max(max_depth, node.depth)
        
        # perform the swap message on current node
        test_message = swap(message, node.get_pairs())
        if num_node_expanded <= 10: # the first 10 expanded node will be remember to memory
            expanded_10_message.append(test_message)
        
        # check if the message is threshold% in dictionary
        percent = count_words(test_message.split(), dict_list)
        if percent >= threshold:
            key = node_to_key(node.get_pairs())
            solution = test_message
            path_cost = node.depth
            break
        
        # append the new node to the fringe
        for child in original_childs:
            new_node = Node(node.get_pairs() + [child])
            
            # calculate h value of new node
            ## swap the frequency in original dictionary accorded to key swap in new node
            new_freq = swap_key_frequency(ORIGINAL_FREQ, new_node.get_pairs())
            ## calculate h value from the new frequency
            h = count_match_freq(new_freq, GOAL_KEY_ORDERING)
            ## set the h value to new node
            new_node.set_h(h)
            
            # add new node to the list with priority queue where smaller h will be on the front
            found = False
            for i in range(len(fringe)):
                if fringe[i].h > new_node.h:
                    fringe.insert(i, new_node)
                    found = True
                    break
            if not found:
                fringe.append(new_node)
                    
        max_fringe_size = max(max_fringe_size, len(fringe))
        
        # break the loop if expanded more than 1000 node
        if num_node_expanded >= 1000:
            break
    
    # gathering output text
    output += print_solution(solution, key, path_cost)
    output += f"Num nodes expanded: {num_node_expanded}\n"
    output += f"Max fringe size: {max_fringe_size}\n"
    output += f"Max depth: {max_depth}\n"
    output += "\n"
        
    return output, expanded_10_message

def a_star():
    return None

class Node():
    def __init__(self, pairs: list, h=0) -> None:
        self.pairs = pairs
        self.depth = len(pairs)
        self.h = h
    
    def get_pairs(self) -> list:
        return self.pairs
    
    def add_pair(self, pair: list) -> None:
        self.pairs.append(pair)
        self.depth = len(self.pairs)
    
    def set_h(self, new_h: int) -> None:
        self.h = new_h

def count_match_freq(original_freq: dict, goal_freq: str) -> int:
    # sort the alphabet by frequency to key string
    sorted_alp = sorted(original_freq.keys(), key=lambda x: (-original_freq[x], x))
    
    # count how many it doesn't match the key
    h = 0
    for i in range(len(sorted_alp)):
        if sorted_alp[i] != goal_freq[i]:
            h += 1
    
    return math.ceil(h/2)

def swap_key_frequency(original_freq: dict, pairs: list) -> dict:
    alp_freq = dict(original_freq)
    for pair in pairs:
        temp = alp_freq[pair[0]]
        alp_freq[pair[0]] = alp_freq[pair[1]]
        alp_freq[pair[1]] = temp
    return alp_freq

def generate_key_frequency(message, key) -> dict:
    alp_freq = {}
    for char in message:
        if char.upper() not in key:
            continue
          
        if char.upper() in alp_freq:
            alp_freq[char.upper()] += 1
        else:
            alp_freq[char.upper()] = 1
    
    return alp_freq

def print_solution(solution, key, path_cost) -> str:
    output = ""
    if solution != "":
        output += f"Solution: {solution}\n"
        output += f"\n"
        output += f"Key: {key}\n"
        output += f"Path Cost: {path_cost}\n"
    else:
        output += "No solution found.\n"
    output += "\n"
    return output

def node_to_key(pairs: list) -> str:
    return ''.join(pair[0] + pair[1] for pair in pairs)

def count_words(message_list: list, dict_list: list) -> int:
    count = sum(1 for word in message_list if word.lower().strip('!()-[]{};:\'",.<>/?@#$%^&*_~') in dict_list)
    percentage = count / len(message_list) * 100
    return percentage

def swap(text: str, pairs: list) -> str:
    for pair in pairs:
        text = text.replace(pair[0].lower(), '\0').replace(pair[1].lower(), pair[0].lower()).replace('\0', pair[1].lower())
        text = text.replace(pair[0].upper(), '\0').replace(pair[1].upper(), pair[0].upper()).replace('\0', pair[1].upper())
    return text

def generate_child(char_list: list) -> list:
    pairs = []
    char_list = list(char_list)
    char_list.sort()
    for i in range(len(char_list)):
        for j in range(i + 1, len(char_list)):
            if char_list[i] == char_list[j]:
                continue
            pair = [char_list[i], char_list[j]]
            pairs.append(pair)
    return pairs

if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task6 function
    print(task6('g', 'secret_msg.txt', 'common_words.txt', 90, 'AENOST', 'n'))
    
    