import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

def match_pattern(input_line: str, pattern: str) -> bool:
    if not pattern:
        return True
    if not input_line:
        return len(pattern) == 1 and pattern[0] == '$'
    
    if pattern[-1] == "$":
        return input_line.endswith(pattern[:-1])
    elif pattern[0] == "^":
        return input_line.startswith(pattern[1:])
    elif len(pattern) > 1 and pattern[1] == "+":
        if pattern[0] != input_line[0]:
            return False
        i = 1
        while i < len(input_line) and input_line[i] == pattern[0]:
            i += 1
        return match_pattern(input_line[i:], pattern[2:])
    elif pattern[0] == input_line[0]:
        return match_pattern(input_line[1:], pattern[1:])
    elif pattern[:2] == "\\d":
        for i, char in enumerate(input_line):
            if char.isdigit():
                if match_pattern(input_line[i+1:], pattern[2:]):
                    return True
        return False
    elif pattern[:2] == "\\w":
        if input_line[0].isalnum():
            return match_pattern(input_line[1:], pattern[2:])
        else:
            return False
    elif pattern[0] == "[" and "]" in pattern:
        end = pattern.index("]")
        if pattern[1] == "^":
            chrs = set(pattern[2:end])
            if input_line[0] in chrs:
                return False
        else:
            chrs = set(pattern[1:end])
            if input_line[0] not in chrs:
                return False
        return match_pattern(input_line[1:], pattern[end+1:])
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
