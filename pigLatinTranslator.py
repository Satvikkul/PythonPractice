# get sentence from user
# split sentence into words
# if starts with vowel just add yay at the end otherwise move first consonant cluster to the end and add ay
# loop through words and convert to pig latin
# stick words into sentence
# output the final string

original = input("Type a sentence that you want to convert: ").strip().lower()


words = original.split()
new_words = []

for word in words:
    if word[0] in 'aeiou':
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in 'aeiou':
                vowel_pos = vowel_pos + 1
            else:
                break
        consonant = word[:vowel_pos]
        rest_word = word[vowel_pos:]
        new_word = rest_word + consonant + "ay"
        new_words.append(new_word)

#print(new_words)
output = " ".join(new_words)
print(output)


