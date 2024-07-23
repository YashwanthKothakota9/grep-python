import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

def match_pattern(input_line: str, pattern: str) -> bool:
    if not input_line and not pattern:
        return True
    if not pattern:
        return True
    if not input_line:
        return False
    if pattern[0] == "^":
        return input_line.startswith(pattern[1:])
    elif pattern[0] == input_line[0]:
        return match_pattern(input_line[1:], pattern[1:])
    elif pattern[:2] == "\\d":
        # In simpler terms, this code is doing the following:
        # It's looking for the first digit in the input line.
        # When it finds a digit, it checks if the rest of the input line from that digit onwards matches the rest of the pattern.
        # If it finds a match, it returns True.
        # If it doesn't find any digits, or if none of the digits lead to a full match, it returns False.
        return next(
            (
                match_pattern(input_line[i:], pattern[2:])
                for i in range(len(input_line))
                if input_line[i].isdigit()
            ),
            False,
        )
    elif pattern[:2] == "\\w":
        if input_line[0].isalnum():
            return match_pattern(input_line[1:], pattern[2:])
        else:
            return False
    elif pattern[0] == "[" and pattern[-1] == "]":
        if pattern[1] == "^":
            chrs = list(pattern[2:-1])
            return all(c not in input_line for c in chrs)
        chrs = list(pattern[1:-1])
        return any(c in input_line for c in chrs)
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
