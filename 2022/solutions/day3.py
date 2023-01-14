from collections import Counter

def get_common_character(compartment1,compartment2):
    for char in compartment1:
        if char in compartment2:
            return char
            

def main():
    priorities = dict()
    for i,char in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        priorities.update({char: i+1})
    for k,v in priorities.items():
        print(f"{k}: {v}")

    # Items in a single rucksack are given on a single line
    # First half of the line is what's in the first compartment
    # Second half of the line....""
    with open('../inputs/day3.txt') as f:
        priorities_list = []
        """
        for line in f:
            # There is only one item that's in both compartments
            letters = list(line)[:-1]
            cut = int(len(letters)/2)
            compartment1 = letters[:cut]
            compartment2 = letters[cut:]
            common_char = get_common_character(compartment1,compartment2)
            p = priorities.get(common_char)
            priorities_list.append(p)
        # Part 1
        print(sum(priorities_list))
        """
        # Part 2
        items = []
        priorities_sum = 0
        for i,line in enumerate(f):
            if not i%3:
                valid_chars = list(line).copy()[:-1]
            else:
                valid_chars = [x for x in line if x in valid_chars]
            print(f"{i} -- {valid_chars}")
            if len(set(valid_chars)) == 1:
                items.append(valid_chars[0])
                print(f"New item: {items[-1]}")
                print(f"Priority: {priorities.get(valid_chars[0])}")
                priorities_sum += priorities.get(valid_chars[0])
        print(f"Final sum: {priorities_sum}")
            
           
if __name__ == "__main__":
    main()
