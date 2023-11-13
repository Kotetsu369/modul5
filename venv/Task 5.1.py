import json

class C1:
    title = '1'
    text = '2'
    author = '3'

    def save(self):
        dictionary = {k: str(v) for k, v in vars(C1).items()}
        with open('file.txt', 'w', encoding='utf-8') as fout:
            json.dump(dictionary, fout)
object = C1()
object.save()
