class Instructor(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.sem = []
        self.subjects = []
        self.dic = {}
    def __str__(self):
        return str(self.name) + str(self.surname) + str(self.dic)
    def kek(self):
        q = int(input('kilkist semestriv'))
        i = 0
        while i < q:
            m = []
            self.sem.append(i+1)
            i += 1
            w = int(input('kilkist predmetiv' + ' ' +str(i) + ' ' + 'semestru'))
            k = 0
            while k<w:
                h = str(input('nazva predmety'))
                m.append(h)
                k += 1
            self.subjects.append(m)
        self.dic = dict(zip((self.sem), self.subjects))
        return self
    def predmetivnasem(self, sem):
        if sem<= len(self.sem):
            return len(self.dic.get(sem))
        else:
            return 'nema takogo semestru'
    def seredne(self):
        p = []
        for i in self.subjects:
            k = len(i)
            p.append(k)
        f = sum(p)
        return float(f/len(self.subjects))
    def maximum(self):
        t=[]
        for item in self.subjects:
            t.append(len(item))
        a = t.index(max(t))
        return self.sem[a]
    def delete(self, sem, subj):
        if sem > len(self.sem):
            return 'nema takogo semestru'
        else:
            try:
                self.subjects[sem-1].remove(subj)
            except ValueError:
                print('nema takogo predmetu')
        return self
    def addd(self, sem, subj):
        if sem > len(self.sem):
            return 'nema takogo semestru'
        else:
            try:
                self.subjects[sem-1].append(subj)
            except ValueError:
                print('nema takogo predmetu')
        return self

a = Instructor('vasya', 'batkovich')
a.kek()
print(a)
# print(a.dic)
print(a.predmetivnasem(3))
print(a.seredne())
print(a.maximum())
# a.delet(2,'b')
# a.addd(1, 'kek')
print(a)
