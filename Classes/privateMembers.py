class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(iter):
        return iter(self.tags)

# use to __ to make private, to alert the consumers not to use it


cloud = TagCloud()
cloud.add("python")
cloud["python"]
cloud.add("python")
cloud.add("python")
