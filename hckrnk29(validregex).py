import re
def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        if re.search(r'[\*\+\?]\+',pattern):
            return False
        return True
        
    except re.error:
        return False
        
n = int(input())
T = [input() for x in range(n)]
for pattern in T:
    if is_valid_regex(pattern):
        print(True)
    else:
        print(False)
