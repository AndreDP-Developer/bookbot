# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

def main():
    path_to_file = "books/frankenstein.txt"
    character_count = {}

    with open(path_to_file) as f:
        file_contents = f.read().lower()
        words = file_contents.split()
        for i in file_contents:
            if i.isalpha():
                if i in character_count:
                    character_count[i] += 1
                else:
                    character_count[i] = 1

    chars_sorted_list = chars_dict_to_sorted_list(character_count)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{len(words)} words found in the document")
    print()

    for c in chars_sorted_list:
        print(f"The '{c['char']}' character was found {c['num']} times")
    #print(character_count)
    print("--- End report ---")

main()