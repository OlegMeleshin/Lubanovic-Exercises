# 15. Create a multi-level dictionary called "Life". Upper-level keys are "animals",
# "plants" and "other". Make "animals" key refer to a dictionary containing
# keys such as "cats", "octopy" and "emus". Make "cats" key refer to a list of
# strings with values "Henru", "Grumpy" and "Lucy". Remaining keys should refer
# to empty dictionaries
cats_list = ['Henri','Grumpy', 'Lucy']
octopy_list = []
emus_list = []

animals_dict = {'cats' : cats_list, 'octopy' : octopy_list, 'emus' : emus_list}
plants_dict = {}
other_dict = {}

life = {'animals' : animals_dict, 'plants' : plants_dict, 'other' : other_dict}

# 16. Print high-level keys of "Life" dictionary
print(f"Dictionary: Life, High-level keys \n{life.keys()}\n")

# 17. Print life['animals'] keys
print(f"Dictionary: Life, section: Animals \n{life['animals'].keys()}\n")

# 18. Print life['animals']['cats'] values 
print(f"Life/Animals/Cats values \n{life['animals']['cats']}\n")
