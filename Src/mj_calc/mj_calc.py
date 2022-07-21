import xlwings as xw

PLAY_POSITION = 'B21'
PEOPLE_POSITION = 'B22'

OLD_POSITION = 2
NEW_POSITION = 11


class Counter:
    def __init__(self, sheet):
        self.sheet = sheet
        self.play_count = int(sheet[PLAY_POSITION].value)
        self.people_count = int(sheet[PEOPLE_POSITION].value)
        print(self.play_count, self.people_count)

    def doStart(self):
        pass


    def getMax(self, play_index):
        pass






#
# don't modify the following code
#

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]

    c = Counter(sheet)
    c.doStart()

@xw.func
def hello(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    xw.Book("mj_calc.xlsm").set_mock_caller()
    main()
