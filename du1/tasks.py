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
    return sum(x * y for x, y in zip(a, b))


def redact(data, chars):
    chars_set = set(chars)
    return "".join('x' if ch in chars_set else ch for ch in data)


def count_words(data):
    if data == "":
        return {}

    counts = {}
    for word in data.split(" "):
        counts[word] = counts.get(word, 0) + 1

    return counts


def bonus_fizzbuzz(num):
    return ('Fizz' * (num % 3 == 0) + 'Buzz' * (num % 5 == 0)) or num


def bonus_utf8(cp):
    if cp < 0 or cp > 0x10FFFF:
        raise ValueError("Error")
    if 0xD800 <= cp <= 0xDFFF:
        raise ValueError("Error")

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
