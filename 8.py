class bank(object):
    cash = 10000
    @classmethod
    def chk_bank(cls):
        print("total cash in bank:",cls.cash)

class andhrabank(bank):
    pass

class statebank(bank):
    cash = 200000
    @classmethod
    def chk_bank(cls):
        print("total cash in state bank:",cls.cash)

a = andhrabank()
a.chk_bank()

s = statebank()
s.chk_bank()