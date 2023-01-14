# https://adventofcode.com/2022/day/1

PATH_TO_INPUT = "../inputs/day1.txt"

def main():
    with open(PATH_TO_INPUT) as f:
        calories_list = []
        current_calories = 0
        for line in f:
            if line == "\n":
                print(f"Current elf calories: {current_calories}")
                calories_list.append(current_calories)
                current_calories = 0
            else:
                current_calories += int(line)
        # Part 1 Answer
        print(f"End max calories: {max(calories_list)}")
        # Part 2 Answer
        print(f"Top 3 calories: {sorted(calories_list)[-3:]}")
        print(f"Sum of top 3 calories: {sum(sorted(calories_list)[-3:])}")

if __name__ == "__main__":
    main()
