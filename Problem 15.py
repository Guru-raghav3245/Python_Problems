def reverse_word(word):
  y = word.split()
  y.reverse()
  return " ".join(y)

print(reverse_word("This is guru"))