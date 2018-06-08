
#!/usr/bin/env python3

import sys

letterValues = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def value_of_roman_letter(ch):
    """Return the value associated with a single Roman numeral letter."""
    try:
        return letterValues[ch.upper()]
    except KeyError:
        print(f"error: invalid Roman numeral character '{ch}'\n",
              file=sys.stderr)
        sys.exit(1)

def int_from_roman_numeral(s):
    """Return the integer value of the given Roman numeral string."""
    result = 0
    lastValue = sys.maxsize
    for ch in s:
        value = value_of_roman_letter(ch)
        if value > lastValue:
            # We've found something like "IV" or "IX"
            # or "XC".  Need to undo the addition
            # of the previous value, then add
            # (value - lastValue) to the result.
            result += value - 2 * lastValue
        else:
            result += value
        lastValue = value
    return result


def convert_to_int(roman_numeral):
    return int_from_roman_numeral(roman_numeral)

