def swap(string, d):
  return_string = ""
  for char in string:
    if char.upper() in d:
      if char.isupper():
        return_string += d[char].upper()
      else:
        return_string += d[char.upper()].lower()
    else:
      return_string += char
  return return_string

def task1(key, filename, indicator):
    #TODO
    return_string = ""
    swap_dict = []
    
    if indicator == "e":
      for i in range(0, len(key), 2):
        d = {}
        d[key[i].upper()] = key[i+1].upper()
        d[key[i+1].upper()] = key[i].upper()
        swap_dict.append(d)
    elif indicator == "d":
      for i in range(len(key) - 1, -1, -2):
        d = {}
        d[key[i].upper()] = key[i-1].upper()
        d[key[i-1].upper()] = key[i].upper()
        swap_dict.append(d)

    with open(filename, "r") as f:
      new_string = f.read()
      for d in swap_dict:
        new_string = swap(new_string, d)
      return_string = new_string
    
    return return_string

if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task1 function
    print(task1('AE', 'spain.txt', 'd'))
    print(task1('VFSC', 'ai.txt', 'd'))
    print(task1('ABBC', 'cabs_plain.txt', 'e'))
    