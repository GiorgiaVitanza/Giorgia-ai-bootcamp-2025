# Implement qui il codice


class Directory:
    def __init__(self):
        self.length = 0
        self.obj = []
        pass

    def __len__(self):
        return self.length

    def add(self, obj):
        self.length += 1
        self.obj.append(obj)

    def query(self, name=""):
        out = []
        for el in self.obj:
            if name == el.name:
                out.append(el)
        return out

    def find(self, string):
        out = []
        for el in self.obj:
            if type(el) == Business:
                if string == el.name or string in el.phone:
                    out.append(el)
            elif type(el) == Person:
                if string == el.name or string == el.surname:
                    out.append(el)
        return out


class Person:
    def __init__(self, name, surname, phone=None):
        self.name = name
        self.surname = surname
        self.phone = phone


class Business:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
