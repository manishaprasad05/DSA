
# 12. Function to count vowels in a string
def vowel(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count += 1

    return count

print("Vowels:",vowel("Welcome Manisha!"))
