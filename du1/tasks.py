def fizzbuzz(num):
    result = "";
    if num % 3 == 0:
        result += "Fizz";
    if num % 5 == 0:
        result += "Buzz";
    if num % 3 != 0 and num % 5 != 0:
        return num;

    return result;
    pass


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    
    for _ in range(2, n + 1):
        a, b = b, a + b
        
    return b


def dot_product(a, b):
    """
    Calculate the dot product of `a` and `b`.
    Assume that `a` and `b` have same length.
    Hint:
        lookup `zip` function
    Example:
        dot_product([1, 2, 3], [0, 3, 4]) == 1*0 + 2*3 + 3*4 == 18
    """
    return sum(x * y for x, y in zip(a, b))


def redact(data, chars):
    """
    Return `data` with all characters from `chars` replaced by the character 'x'.
    Characters are case sensitive.
    Example:
        redact("Hello world!", "lo")        # Hexxx wxrxd!
        redact("Secret message", "mse")     # Sxcrxt xxxxagx
    """
    chars_set = set(chars)
    return "".join('x' if ch in chars_set else ch for ch in data)


def count_words(data):
    """
    Return a dictionary that maps word -> number of occurences in `data`.
    Words are separated by spaces (' ').
    Characters are case sensitive.

    Hint:
        "hi there".split(" ") -> ["hi", "there"]

    Example:
        count_words('this car is my favourite what car is this')
        {
            'this': 2,
            'car': 2,
            'is': 2,
            'my': 1,
            'favourite': 1,
            'what': 1
        }
    """
    if data == "":
        return {}

    counts = {}
    for word in data.split(" "):
        counts[word] = counts.get(word, 0) + 1

    return counts


def bonus_fizzbuzz(num):
    """
    Implement the `fizzbuzz` function.
    `if`, match-case and cycles are not allowed.
    """
    return ('Fizz' * (num % 3 == 0) + 'Buzz' * (num % 5 == 0)) or num


def bonus_utf8(cp):
    """
    Encode `cp` (a Unicode code point) into 1-4 UTF-8 bytes - you should know this from `Základy číslicových systémů (ZDS)`.
    Example:
        bonus_utf8(0x01) == [0x01]
        bonus_utf8(0x1F601) == [0xF0, 0x9F, 0x98, 0x81]
    """
    if cp < 0 or cp > 0x10FFFF:
        raise ValueError("Invalid Unicode code point")
    if 0xD800 <= cp <= 0xDFFF:
        raise ValueError("Surrogate code points are not valid Unicode scalar values")

    if cp <= 0x7F:
        return [cp]
    if cp <= 0x7FF:
        return [
            0xC0 | (cp >> 6),
            0x80 | (cp & 0x3F)
        ]
    if cp <= 0xFFFF:
        return [
            0xE0 | (cp >> 12),
            0x80 | ((cp >> 6) & 0x3F),
            0x80 | (cp & 0x3F)
        ]

    return [
        0xF0 | (cp >> 18),
        0x80 | ((cp >> 12) & 0x3F),
        0x80 | ((cp >> 6) & 0x3F),
        0x80 | (cp & 0x3F)
    ]
