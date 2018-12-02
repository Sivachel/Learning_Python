#If statements
is_male = True
is_tall = True
if is_male or is_tall: # use "or" for anyone of the condition to be true. Use "and" for both condition to be true.
    print("you are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("you are not a male or tall ")
