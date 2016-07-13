import random
class GroupAssigner:
    '''GroupAssigner class
    takes roster - string of filename with list of students, names separated by linebreaks
    '''
    def __init__(self, roster):

        roster_file = open(roster, 'r')
        self.roster = roster_file.read().splitlines()
        self.students = len(self.roster)

    '''make groups from roster.
    takes group_size - integer size of each group_size
    takes autofix - boolean to tell program if it should deal with leftover person/small group_size
    '''
    def make_groups(self, group_size, autofix):
        students = list(self.roster)
        random.shuffle(students)
        groups = []

        while students:
            group = []
            for i in range(group_size):
                if len(students) == 0:
                    break
                group.append(students.pop())
            groups.append(group)

        if autofix:
            return self.fix_groups(groups)
        else:
            return groups

    ''' prevent groups of only 1 person from being formed'''

    def fix_groups(self, groups):
        fixed_groups = list(groups)
        # prohibit group of only one person
        for group in fixed_groups:
            if len(group) == 1:
                lone_student = group[0]
                fixed_groups.remove(group)
                random.shuffle(fixed_groups)
                fixed_groups[0].append(lone_student)
        return groups

# script 
group_size = int(input("Group size?"))
autofix = int(input("Autofix? 0 for false, 1 for true"))

g = GroupAssigner('roster.txt')
groups = g.make_groups(group_size, bool(autofix))

print(groups)
