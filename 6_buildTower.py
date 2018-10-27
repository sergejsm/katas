def tower_builder(n_floors):

    tower = list()
    for floor in range(n_floors, 0, -1):
        starNumb = floor*2 -1
        spaceNumb = ((n_floors * 2 - 1) - starNumb) // 2
        strToInsert = " "*spaceNumb + "*"*starNumb + " "*spaceNumb
        tower.insert(0, strToInsert)

    return '\n'.join(tower)

print(tower_builder(10))

#Best Solution:
def tower_builder2(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


def tower_builder3(n):
    return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]