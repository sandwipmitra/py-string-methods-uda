my_txt = "mitra has {} cats and {} dog"
print(my_txt.format("7", "1"))

my_string = "I love {} and {}"
print(my_string.format("computer science", "python programming"))

#String
new_str = "The cow jumped over the moon."
new_str.split()
#Output is:
# ```Python
# ['The', 'cow', 'jumped', 'over', 'the', 'moon.']```

# 2. Here  the separator is space, and the maxsplit argument is set to 3.
#     ```Python
new_str.split(' ', 3)
#Output is:
# ```Python
# ['The', 'cow', 'jumped', 'over the moon.']```

# 3. Using '.' or period as a separator.
# ```Python
new_str.split('.')
# Output is:
# ```Python
# ['The cow jumped over the moon', '']```

# 4. Using no separators but having a maxsplit argument of 3.
#     ```Python
new_str.split(None, 3)
#     Output is:
#     ```Python
# ['The', 'cow', 'jumped', 'over the moon.']``

#--------exercises-------
# verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
# your_string = len(verse)
# your_index = verse.index("and")
# your_index_2 = verse.index("can")
# # your_index_3 = verse.index("you", last)
# yor_count = verse.count("you")
# print(your_string)
# print(your_index)
# print(your_index_2)
# # print(your_index_3)
# print(yor_count)



verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"

#print(verse, "\n")

# print("Verse has a length of {} characters.".format(len(verse)))
# print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
# print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
# print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))


print("{}".format(len(verse)))
print("{}".format(verse.find("and")))
print("{}".format(verse.rfind("you")))
print("{}".format(verse.count("you")))

