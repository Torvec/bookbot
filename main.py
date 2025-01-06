def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    word_count = get_num_words(text)
    char_count = get_num_chars(text)
    char_count_list = convert_to_list(char_count)
    sorted_char_count_list = sorted(char_count_list, reverse=True, key=sort_on)
    report = print_report(sorted_char_count_list)
    
    print(f"=== Begin report of {file_path} ===\n")
    print(f"{word_count} words found in the document\n\n")
    print(report)
    print("=== End Report ===")

def print_report(sorted_list):    
    report = ""
    for char in sorted_list:
        letter = char["letter"]
        count = char["count"]
        report += f"The {letter} letter was found {count} times.\n"
    return report

def sort_on(item):
    return item["count"]

def convert_to_list(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"letter": key, "count": value})
    return dict_list

def get_num_chars(text):
    char_count = {}
    for t in text:
        lower_t = t.lower()
        if lower_t.isalpha():
            if lower_t in char_count:
                char_count[lower_t] += 1
            else:
                char_count[lower_t] = 1
    return char_count

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()
