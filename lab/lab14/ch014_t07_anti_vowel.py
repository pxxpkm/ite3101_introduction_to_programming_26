def anti_vowel(text):
    result = ""
    for char in text:
        if char not in "aeiouAEIOU":
            result += char
    return result
