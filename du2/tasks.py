import dataclasses
from typing import Callable, Generic, List, Optional, TypeVar


def cached(f):
    cache = {}
    order = []

    def wrapper(*args):
        if args in cache:
            return cache[args]
        
        result = f(*args)
        
        if len(cache) >= 3:
            oldest_key = order.pop(0)
            del cache[oldest_key]
        
        cache[args] = result
        order.append(args)

        return result
    
    return wrapper

        

T = TypeVar("T")


@dataclasses.dataclass
class ParseResult(Generic[T]):
    value: Optional[T]
    rest: str

    @staticmethod
    def invalid(rest: str) -> "ParseResult":
        return ParseResult(value=None, rest=rest)

    def is_valid(self) -> bool:
        return self.value is not None

Parser = Callable[[str], ParseResult[T]]


def parser_char(char: str) -> Parser[str]:
    if len(char) != 1:
        raise ValueError()

    def parse(s: str) -> ParseResult[str]:
        if s and s[0] == char:
            return ParseResult(value=char, rest=s[1:])
        return ParseResult.invalid(s)
    
    return parse


def parser_repeat(parser: Parser[T]) -> Parser[List[T]]:
    def parse(s: str) -> ParseResult[List[T]]:
        results = []
        rest = s
        while True:
            res = parser(rest)
            if not res.is_valid():
                break
            results.append(res.value)
            rest = res.rest
        return ParseResult(value=results, rest=rest)
    return parse


def parser_seq(parsers: List[Parser]) -> Parser:
    def parse(s: str):
        results = []
        rest = s
        for p in parsers:
            res = p(rest)
            if not res.is_valid():
                return ParseResult.invalid(s)
            results.append(res.value)
            rest = res.rest
        return ParseResult(value=results, rest=rest)
    return parse


def parser_choice(parsers: List[Parser]) -> Parser:
    def parse(s: str):
        for p in parsers:
            res = p(s)
            if res.is_valid():
                return res
        return ParseResult.invalid(s)
    return parse


R = TypeVar("R")

def parser_map(parser: Parser[R], map_fn: Callable[[R], Optional[T]]) -> Parser[T]:
    def parse(s: str):
        res = parser(s)
        if not res.is_valid():
            return ParseResult.invalid(s)
        
        mapped_value = map_fn(res.value)
        
        if mapped_value is None:
            return ParseResult.invalid(s)
            
        return ParseResult(value=mapped_value, rest=res.rest)
    return parse


def parser_matches(filter_fn: Callable[[str], bool]) -> Parser[str]:
    def parse(s: str):
        if s and filter_fn(s[0]):
            return ParseResult(value=s[0], rest=s[1:])
        return ParseResult.invalid(s)
    return parse


def parser_string(string: str) -> Parser[str]:
    char_parsers = [parser_char(c) for c in string]
    seq_parser = parser_seq(char_parsers)
    return parser_map(seq_parser, lambda chars: "".join(chars))


def parser_int() -> Parser[int]:
    digit_parser = parser_matches(lambda c: c.isdigit())
    digits_parser = parser_repeat(digit_parser)
    return parser_map(digits_parser, lambda chars: int("".join(chars)) if chars else None)