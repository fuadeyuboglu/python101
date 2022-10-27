# A comfortable word is a word which you can type always alternating the hand you type with (Q-keybord)


left = {"q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"}
right = {"y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"}

word = input("Please enter a word: ").lower()
word_set = set(word)

print("\n")

if right.intersection(word_set) and left.intersection(word_set):
    print(True, f"'{word}' is a comfortable word.")
elif right.intersection(word_set):
    print(False, "(uses only right-hand fingers)")
else:
    print(False, "(uses only left-hand fingers)" )
