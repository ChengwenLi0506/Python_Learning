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
        self.setName()
        for i in range(1,self.play_count + 1):
            self.getMax(i)
        self.countBigWinner()

    def getMax(self, play_index):
        Max = 0
        index = 0
        column = self.changeNumToChar(play_index)
        for i in range(self.people_count):
            position = column + str(i + OLD_POSITION)
            if self.sheet[position].value is not None:
                if self.sheet[position].value > Max:
                    Max = self.sheet[position].value
                    index = i
        self.sheet[column + str(index + NEW_POSITION)].value = 1

    def setName(self):
        for i in range(self.people_count):
            before = 'B' + str(OLD_POSITION + i)
            after = 'B' + str(NEW_POSITION + i)
            self.sheet[after].value = self.sheet[before].value

    def changeNumToChar(self, play = None):
        if play <= 24:
            return chr(play + 66)
        else:
            return 'A' + chr(play + 40)

    def countBigWinner(self):
        big_winner = self.changeNumToChar(self.play_count + 2)
        for i in range (NEW_POSITION, NEW_POSITION + self.people_count):
            count = 0
            for j in range(1,self.play_count+1):
                column = self.changeNumToChar(j)
                position = column + str(i)
                if self.sheet[position].value is not None:
                    count += self.sheet[position].value
            self.sheet[big_winner + str(i - (self.people_count + 3))].value = count


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
