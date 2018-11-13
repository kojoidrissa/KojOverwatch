from overwatch import Overwatch
kojo = Overwatch(battletag="kojoidrissa#1291")

with open("overwatch_methods.txt", 'w') as attributes_file:
    attributes_file.write(str(dir(kojo)))
    # 2018-11-12 Notes: Figure out how to print help for each attribute on the Overwatch object
    # for attribute in dir(kojo):
    #     attributes_file.write(help(kojo.))

support_list = [
    "ana",
    "lucio",
    "brigitte",
    "moira",
    "zenyatta"
]
with open("overwatch_stats.txt", 'w') as stats_file:
    stats_file.write("\nOVERALL STATS\n" + str(kojo()))
    stats_file.write("\n\nGENERAL STATS\n")
    for hero in support_list:
        stats_file.write(f"\n{hero}\n".upper() + str(kojo(hero=hero, filter="hero specific")))
    stats_file.write("\n\nCOMBAT STATS\n")
    for hero in support_list:
        stats_file.write(f"\n{hero}\n".upper() + str(kojo(hero=hero, filter="combat")))


# 2018-11-12 Notes: Why is this giving me an IndexError: list index out of range? 
# The problem is at line 75, in _generate_comparisons
# print(kojo.playtime)
# print(help(kojo._generate_comparisons))
