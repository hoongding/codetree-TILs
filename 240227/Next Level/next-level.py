class Codetree:
    def __init__(self, _id, level):
        self._id = _id
        self.level = level
    def _print(self):
        print(f'user {self._id} lv {self.level}')

nickname, level = tuple(input().split())

codetree = Codetree('codetree', 10)
_input = Codetree(nickname, level)

codetree._print()
_input._print()