class A:
    def __init__(self):
        self.resp = 'Response'

    def sum(self):
        resp = self.resp
class B(A):
    def valprint(self):
        print('My Value is VAL')
