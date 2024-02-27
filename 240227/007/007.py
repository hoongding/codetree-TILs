class Secret:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time
    def _print(self):
        print(f'secret code : {self.code}')
        print(f'meeting point : {self.place}')
        print(f'time : {self.time}')
    

code, place, time = tuple(input().split())

s = Secret(code, place, time)

s._print()