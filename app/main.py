import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

class Pattern:
    DIGIT = '\\d'
    ALNUM = '\\w'


def match_pattern(input_line, pattern):
    if len(input_line) == 0 and len(pattern) == 0:
        return True
    if not pattern:
        return True
    if not input_line:
        return False
    
    if pattern[0] == input_line[0]:
        return match_pattern(input_line[1:], pattern[1:])
    elif pattern[:2] == Pattern.DIGIT:
        for i in range(len(input_line)):
            if input_line[i].isdigit():
                return match_pattern(input_line[i:], pattern[2:])
            else:
                return False
    elif pattern[:2] == Pattern.ALNUM:
        if input_line[0].isalnum():
            return match_pattern(input_line[1:], pattern[2:])
        else:
            return False
    elif pattern[0] == '[' and pattern[-1] == ']':
        if pattern[1] == '^':
            chars = list(pattern[2:-1])
            for c in chars:
                if c in input_line:
                    return False
            return True
        chars = list(pattern[1:-1])
        for c in chars:
            if c in input_line:
                return True
        return False
    else:
        return match_pattern(input_line[1:], pattern)


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
