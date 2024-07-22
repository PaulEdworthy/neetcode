
def is_valid(s: str):
    stack = []
    matches = {'()', '{}', '[]'}

    for ch in s:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack or (stack.pop() + ch) not in matches:
                print(False)
                return False
    print(True)
    return not stack


a = '()'  # true
b = '()[]{}'  # true
c = '(]'  # false

is_valid(a)
is_valid(b)
is_valid(c)
