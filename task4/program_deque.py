import itertools
from collections import deque 
import time

def task4(algorithm, message_filename, dictionary_filename, threshold, letters, debug):
    
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
        output, expanded_10_message = ids(message, dict_list, threshold, first_child)
    elif algorithm == 'u':
        output, expanded_10_message = ucs(message, dict_list, threshold, first_child)

    if debug == 'y':
        output += "\n\n"
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
    fringe = deque([Node([])])
    
    while True:
        # get the first element on the list and delete it
        num_node_expanded += 1
        node = fringe.popleft()
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
            fringe.appendleft(new_node)
        max_fringe_size = max(max_fringe_size, len(fringe))
        
        # break the loop if expanded more than 1000 node
        if num_node_expanded >= 1000:
            break
    
    # gathering output text
    output += print_solution(solution, key, path_cost)
    output += f"Num nodes expanded: {num_node_expanded}\n"
    output += f"Max fringe size: {max_fringe_size}\n"
    output += f"Max depth: {max_depth}"
        
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
    fringe = deque([Node([])])
    
    while True:
        # get the first element on the list and delete it
        num_node_expanded += 1
        node = fringe.popleft()
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
    output += f"Max depth: {max_depth}"
        
    return output, expanded_10_message

def ids(message, dict_list, threshold, original_childs):

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

    for depth_limit in itertools.count():
        fringe = deque([Node([])])
        while fringe:
            num_node_expanded += 1
            node = fringe.popleft()
            max_depth = max(max_depth, node.depth)
            test_message = swap(message, node.get_pairs())
            if num_node_expanded <= 10:
                expanded_10_message.append(test_message)
            percent = count_words(test_message.split(), dict_list)
            if percent >= threshold:
                key = node_to_key(node.get_pairs())
                solution = test_message
                path_cost = node.depth
                break
            if node.depth < depth_limit:
                for child in reversed(original_childs):
                    new_node = Node(node.get_pairs() + [child])
                    fringe.appendleft(new_node)
            max_fringe_size = max(max_fringe_size, len(fringe))
            if num_node_expanded >= 1000:
                break
        
        if solution:
            break
        
    # gathering output text
    output += print_solution(solution, key, path_cost)
    output += f"Num nodes expanded: {num_node_expanded}\n"
    output += f"Max fringe size: {max_fringe_size}\n"
    output += f"Max depth: {max_depth}"
    return output, expanded_10_message

def ucs(message, dict_list, threshold, original_childs):

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
    fringe = deque([Node([])])

    while fringe:
        node = fringe.popleft()
        num_node_expanded += 1
        max_depth = max(max_depth, node.depth)
        test_message = swap(message, node.get_pairs())
        if num_node_expanded <= 10:
            expanded_10_message.append(test_message)
        percent = count_words(test_message.split(), dict_list)
        if percent >= threshold:
            key = node_to_key(node.get_pairs())
            solution = test_message
            path_cost = node.depth
            break
        for child in original_childs:
            new_node = Node(node.get_pairs() + [child])
            fringe.append(new_node)
        max_fringe_size = max(max_fringe_size, len(fringe))
        if num_node_expanded >= 1000:
            break
    
    # gathering output text
    output += print_solution(solution, key, path_cost)
    output += f"Num nodes expanded: {num_node_expanded}\n"
    output += f"Max fringe size: {max_fringe_size}\n"
    output += f"Max depth: {max_depth}"
    return output, expanded_10_message

class Node():
    def __init__(self, pairs: list) -> None:
        self.pairs = pairs
        self.depth = len(pairs)
    
    def get_pairs(self) -> list:
        return self.pairs
    
    def add_pair(self, pair: list) -> None:
        self.pairs.append(pair)
        self.depth = len(self.pairs)
        
    def __repr__(self):
        return "Node: " + str(self.pairs)

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
    # Example function calls below, you can add your own to test the task4 function
    start_time = time.time()  # Get the current time in seconds
    print(task4('d', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    end_time = time.time()  # Get the current time after the function completes
    # Calculate the runtime
    runtime = end_time - start_time
    print(f"Runtime of dfs: {runtime} seconds")

    print(task4('b', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    print(task4('i', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    print(task4('u', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    