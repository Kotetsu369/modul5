class StringVar:

    def __init__(self, t:str):
        self.t = t
    def set(self,change):
        self.t = change
    def get(self):
        return self.t

t = StringVar(input('введите текст'))
#input('введите текст2')
#t = t.change
print(t.set(input('введите изменение')))
print(t.get())
