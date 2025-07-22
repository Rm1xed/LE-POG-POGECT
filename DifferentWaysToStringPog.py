## Python String testing
text = "  Hello World! Python is THE POG  "
email = "POGITAS@gmole.con"
numbers = "123456789"
mixed = "Hello123pog"

print("=" * 50)
print("CASE pog METHODS")
print("=" * 50)

## Case pogging
print(f"Original: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"title(): '{text.title()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"swapcase(): '{text.swapcase()}'")
print(f"casefold(): '{text.casefold()}'")  # More aggressive lowercase

print("\n" + "=" * 50)
print("WHITESPACE METHODS")
print("=" * 50)

## Whitespace pogging
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")
print(f"strip('! '): '{text.strip('! ')}'")  # Custom characters

print("\n" + "=" * 50)
print("ALIGNMENT & PoDgING METHODS")
print("=" * 50)

word = "Python"
print(f"Original: '{word}'")
print(f"center(20): '{word.center(20)}'")
print(f"center(20, '*'): '{word.center(20, '*')}'")
print(f"ljust(20): '{word.ljust(20)}'")
print(f"ljust(20, '-'): '{word.ljust(20, '-')}'")
print(f"rjust(20): '{word.rjust(20)}'")
print(f"rjust(20, '+'): '{word.rjust(20, '+')}'")
print(f"zfill(10): '{numbers.zfill(10)}'")

print("\n" + "=" * 50)
print("SEARCH & CHECK METHODS")
print("=" * 50)

sample = "Hello World Hello Python"
print(f"Text: '{sample}'")
print(f"find('Hello'): {sample.find('Hello')}")
print(f"find('Hello', 5): {sample.find('Hello', 5)}")
print(f"rfind('Hello'): {sample.rfind('Hello')}")
print(f"index('World'): {sample.index('World')}")
print(f"count('Hello'): {sample.count('Hello')}")
print(f"startswith('Hello'): {sample.startswith('Hello')}")
print(f"endswith('Python'): {sample.endswith('Python')}")
print(f"'World' in sample: {'World' in sample}")

print("\n" + "=" * 50)
print("BOOLEAN CHECK METHODS")
print("=" * 50)

test_strings = ["abc123", "ABC", "123", "abc", "   ", "Hello World", "hello_world"]

for s in test_strings:
    print(f"\nString: '{s}'")
    print(f"  isalnum(): {s.isalnum()}")    # Letters and digits
    print(f"  isalpha(): {s.isalpha()}")    # Only letters
    print(f"  isdigit(): {s.isdigit()}")    # Only digits
    print(f"  isnumeric(): {s.isnumeric()}")  # Numeric characters
    print(f"  isspace(): {s.isspace()}")    # Only whitespace
    print(f"  islower(): {s.islower()}")    # All lowercase
    print(f"  isupper(): {s.isupper()}")    # All uppercase
    print(f"  istitle(): {s.istitle()}")    # Title case
    print(f"  isidentifier(): {s.isidentifier()}")  # Valid Python identifier

print("\n" + "=" * 50)
print("SPLIT & JOIN METHODS")
print("=" * 50)

sentence = "apple,banana,cherry,date"
words = "The quick brown fox"
print(f"Original: '{sentence}'")
print(f"split(','): {sentence.split(',')}")
print(f"split(',', 2): {sentence.split(',', 2)}")  # Max splits
print(f"rsplit(',', 1): {sentence.rsplit(',', 1)}")  # Right split

print(f"\nWords: '{words}'")
print(f"split(): {words.split()}")  # Split on any whitespace

## Join examples
fruits = ['apple', 'banana', 'cherry']
print(f"\nList: {fruits}")
print(f"', '.join(fruits): {', '.join(fruits)}")
print(f"' | '.join(fruits): {' | '.join(fruits)}")

## Partition and rpartition
text_part = "name=value=extra"
print(f"\nText: '{text_part}'")
print(f"partition('='): {text_part.partition('=')}")
print(f"rpartition('='): {text_part.rpartition('=')}")

print("\n" + "=" * 50)
print("REPLACEMENT METHODS")
print("=" * 50)

text_replace = "Hello World, Hello Universe"
print(f"Original: '{text_replace}'")
print(f"replace('Hello', 'Hi'): '{text_replace.replace('Hello', 'Hi')}'")
print(f"replace('Hello', 'Hi', 1): '{text_replace.replace('Hello', 'Hi', 1)}'")  # Max replacements

## Translation table
translation_table = str.maketrans('aeiou', '12345')
print(f"translate(vowels to numbers): '{text_replace.translate(translation_table)}'")

## Remove characters
remove_table = str.maketrans('', '', 'aeiou')
print(f"translate(remove vowels): '{text_replace.translate(remove_table)}'")

print("\n" + "=" * 50)
print("ENCODING & FORMATTING METHODS")
print("=" * 50)

## Encoding/decoding
text_encode = "Hello POGS"
print(f"Original: '{text_encode}'")
encoded = text_encode.encode('utf-8')
print(f"encode('utf-8'): {encoded}")
print(f"decode back: '{encoded.decode('utf-8')}'")

## String formatting methods
template = "Hello {name}, you are {age} years old"
print(f"\nTemplate: '{template}'")
print(f"format(): '{template.format(name='Krishna', age=30)}'")

## Format with positional porgs
template2 = "Hello {bitch}, you are {1} years old"

## Format pog
data = {'name': 'Amartya', 'age': 2}
print(f"format_map(): '{template.format_map(data)}'")

print("\n" + "=" * 50)
print("ADVANCED STRING METHODS")
print("=" * 50)

## Expongs
tabbed = "Name\tAge\tCity"
print(f"Original: '{tabbed}'")
print(f"expandtabs(): '{tabbed.expandtabs()}'")
print(f"expandtabs(4): '{tabbed.expandtabs(4)}'")

## Splitline pog
multiline = "Line 1\nLine 2\r\nLine 3\rLine 4"
print(f"\nMultiline text splitlines(): {multiline.splitlines()}")
print(f"splitlines(keepends=True): {multiline.splitlines(keepends=True)}")

## String formatting with format poggers
number = 42
pi = 3.14159
print(f"\nNumber formatting:")
print(f"'{number:>10}'")    ### Right align in 10 chars
print(f"'{number:<10}'")    ### Left align in 10 chars
print(f"'{number:^10}'")    ### Center align in 10 chars
print(f"'{number:0>10}'")   ### Right align, pad with zeros
print(f"'{pi:.2f}'")        ### 2 decimal places
print(f"'{pi:>10.2f}'")     ### Right align, 2 decimal places

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

## Email validation POGGER
def is_valid_email_format(email):
    return email.count('@') == 1 and '.' in email.split('@')[1]

## Password strength POG
def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = not password.isalnum()
    return all([has_upper, has_lower, has_digit, has_special, len(password) >= 8])

## Text pogging
def clean_text(text):
    return ' '.join(text.strip().split())

## Examples of POG
emails = ["user@domain.com", "invalid.email", "test@site.co.in"]
passwords = ["Password123!", "weak", "Strong@Pass1"]
messy_text = "  Too   many    pogging    spaces   here  "

print("Email validation:")
for e in emails:
    print(f"  {e}: {is_valid_email_format(e)}")

print("\nPassword strength:")
for p in passwords:
    print(f"  {p}: {check_password_strength(p)}")

print(f"\nText cleaning:")
print(f"  Before: '{messy_text}'")
print(f"  After:  '{clean_text(messy_text)}'")

print("\n" + "=" * 50)
print("STRING METHOD CHAINING")
print("=" * 50)

messy_input = "  HELLO world! THIS is PogTHON  "
cleaned = messy_input.strip().lower().replace('!', '').title()
print(f"Original: '{messy_input}'")
print(f"Chained:  '{cleaned}'")

## chaining THE POG
data = "apple,BANANA,Cherry,DATE"
result = ', '.join(item.strip().title() for item in data.split(','))
print(f"\nData processing:")
print(f"Input:  '{data}'")
print(f"Output: '{result}'")