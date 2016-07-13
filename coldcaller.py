import random
class ColdCaller:
    '''ColdCaller class
    takes roster - string of filename with list of students, names separated by linebreaks
    '''
    def __init__(self, roster):

        roster_file = open(roster, 'r')
        self.roster = roster_file.read().splitlines()
        self.students = len(self.roster)

    '''Call on a student from roster randomly'''
    def call(self):
        randIndex = random.randint(0, self.students - 1)
        return self.roster[randIndex]


caller = ColdCaller('roster.txt')
print(caller.call())
