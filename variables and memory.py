x = 23
print(id(x))
y = 23
print(id(y))
x = x + 1
print(id(x))

dan = 'student'
print(id(dan))

class VisitCards:
    pass


visit_c = VisitCards()
print(type(visit_c))
print(id(visit_c))
