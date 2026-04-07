#write a code to check given word is palindrome or not
word = "mam"
word1 = word[::-1]
if word == word1:
  print("Palindrome")
else:
  print("Not a palindrome")
