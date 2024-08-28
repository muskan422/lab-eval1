def count_v(text):
    vowels = 'aeiouAEIOU'
    vowel_c = 0
    unique_v = set()

    for char in text:
        if char in vowels:
            vowel_c += 1
            unique_v.add(char.lower())

    return vowel_c, unique_v


text = input("Enter text\n")

vowel_c, unique_v = count_v(text)
print(f"Vowels: {vowel_c}")
print(", ".join(sorted(unique_v)))



#We are Developers
