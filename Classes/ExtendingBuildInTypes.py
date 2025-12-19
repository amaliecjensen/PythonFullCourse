class Text(str):
    def duplicate(self):
        return self+self  # concatinating a string with itself


text = Text("python")
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("append called")
        super().append(object)


list = TrackableList()
list.append("1")
