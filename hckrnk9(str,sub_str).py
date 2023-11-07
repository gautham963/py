import re
def count_substring(string, sub_string):
    pattern = re.compile(f'(?=({sub_string}))')
    matches = re.finditer(pattern, string)

    count = 0
    for match in matches:
        count += 1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
