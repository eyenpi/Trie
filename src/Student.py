class Student:
    def __init__(self, name, number, gpa, field):
        self.name = name
        self.number = number
        self.gpa = gpa
        self.field = field

    def __hash__(self):
        hashed = 0

        # first method that was my idea
        # r = 0
        # for i in self.number:
        #     hashed += int(i) * 31 ** r
        #     r += 1

        # the method I found later
        for i in self.number:
            hashed = int(i) + (hashed * 33) + (hashed * 97)

        # third method
        # for i in self.number:
        #     hashed = ((hashed << 4) + hashed) ^ int(i)

        return hashed
