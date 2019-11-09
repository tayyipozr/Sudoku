from constraint import *

problem = Problem()
oToN = [1, 2, 3, 4, 5, 6, 7, 8, 9]
varible_list = []
for i in range(81):
    varible_list.append(i)

problem.addVariables(varible_list, oToN)

column_list = list((range(0, 73, 9)))

basla = 0
bitir = 81
atla = 9
liste = []
liste1 = []

for i in oToN:
    liste.append(list((range(basla, bitir, atla))))
    problem.addConstraint(AllDifferentConstraint(), list(range(column_list[i - 2], column_list[i - 1])))
    problem.addConstraint(AllDifferentConstraint(), list((range(basla, bitir, atla))))


    basla += 1
    bitir += 1


def listeee(liste):
    for i in range(0, 9, 3):
        liste1.append(liste[i][:3] + liste[(i + 1)][:3] + liste[i + 2][:3])
        liste1.append(liste[i][3:6] + liste[i + 1][3:6] + liste[i + 2][3:6])
        liste1.append(liste[i][6:9] + liste[i + 1][6:9] + liste[i + 2][6:9])
    return liste1

list2 = listeee(liste)

for i in oToN:
    problem.addConstraint(AllDifferentConstraint(), list2[i - 1])

problem.addConstraint(lambda a: a == 7, varible_list[3])
problem.addConstraint(lambda a: a == 1, varible_list[9])
problem.addConstraint(lambda a: a == 4, varible_list[21])
problem.addConstraint(lambda a: a == 3, varible_list[22])
problem.addConstraint(lambda a: a == 2, varible_list[24])
problem.addConstraint(lambda a: a == 6, varible_list[35])
problem.addConstraint(lambda a: a == 5, varible_list[39])
problem.addConstraint(lambda a: a == 9, varible_list[41])
problem.addConstraint(lambda a: a == 4, varible_list[51])
problem.addConstraint(lambda a: a == 1, varible_list[52])
problem.addConstraint(lambda a: a == 8, varible_list[53])
problem.addConstraint(lambda a: a == 8, varible_list[58])
problem.addConstraint(lambda a: a == 1, varible_list[59])
problem.addConstraint(lambda a: a == 2, varible_list[65])
problem.addConstraint(lambda a: a == 5, varible_list[70])
problem.addConstraint(lambda a: a == 4, varible_list[73])
problem.addConstraint(lambda a: a == 3, varible_list[78])

solution = problem.getSolution()
