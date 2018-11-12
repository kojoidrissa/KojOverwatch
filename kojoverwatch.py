from overwatch import Overwatch
kojo = Overwatch(battletag="kojoidrissa#1291")

with open("overwatch_methods.txt", 'w') as file:
    file.write(str(dir(kojo)))
    # 2018-11-12 Notes: Figure out how to print help for each attribute on the Overwatch object
    # for attribute in dir(kojo):
    #     file.write(help(kojo.))

print(kojo())

# 2018-11-12 Notes: Why is this giving me an IndexError: list index out of range? 
# The problem is at line 75, in _generate_comparisons
# print(kojo.playtime)
print(help(kojo._generate_comparisons))
