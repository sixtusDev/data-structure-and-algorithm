class HashMap:
    def __init__(self, size) -> None:
        self.size = size
        self.map = [None] * self.size

    def _generate_hash(self, key) -> int:
        hash_key = 0
        for char in key:
            hash_key += ord(char)
        return hash_key % self.size

    def __setitem__(self, key, value) -> None:
        hash_key = self._generate_hash(key)
        key_value = [key, value]

        if self.map[hash_key] is None:
            self.map[hash_key] = list([key_value])
            return

        for pair in self.map[hash_key]:
            if pair[0] == key:
                pair[1] = value
                return
        
        self.map[hash_key].append(key_value)
        return

    def __getitem__(self, key) -> int:
        hash_key = self._generate_hash(key)
        list_item = self.map[hash_key]
        
        if list_item is None:
            return

        if list_item is not None:
            for pair in list_item:
                if pair[0] == key:
                    return pair[1]

    def delete(self, key) -> None:
        hash_key = self._generate_hash(key)

        if self.map[hash_key] is None:
            return

        for i in range(0, len(self.map[hash_key]) - 1):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key].pop(i)

    def print(self):
        print(self.map)



ages = HashMap(10)
ages["frank"] = 10
ages["grace"] = 20
ages["maggie"] = 40
ages["john"] = 30
ages["jay"] = 18
ages["peter"] = 29
print(ages["jay"])
print(ages["frank"])
ages.delete("maggie")
ages.delete("grace")
ages.print()


        