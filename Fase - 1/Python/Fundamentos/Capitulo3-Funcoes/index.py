import math

def repeat_lyrics():
    print_lyrics()
    print_lyrics()



def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
#print(print_lyrics)
#repeat_lyrics()

def print_twice(bruce):
    print(bruce)
    print(bruce)


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

#cat_twice(2,3)

result = print_twice(print_lyrics)
print(result)