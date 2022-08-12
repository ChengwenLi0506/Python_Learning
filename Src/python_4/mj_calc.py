import xlwings as xw

PLAY_POSITION = 'B21'
PEOPLE_POSITION = 'B22'

OLD_PEOPLE_POSITION = 2
NEW_PEOPLE_POSITION = 11

PLAY_NAME_POSITION = 2


class Counter:
    def __init__(self, sheet):
        self.sheet = sheet
        self.play_count = int(sheet[PLAY_POSITION].value)
        self.people_count = int(sheet[PEOPLE_POSITION].value)

    def doStart(self):
        # clear the original content
        self.clear()

        # copy people name
        self.copyName()

        # operate the big winner
        self.calcWinner()
        self.sumWinner()


    # clear the winner's calculation region
    def clear(self):
        c = PLAY_NAME_POSITION
        r = NEW_PEOPLE_POSITION
        start = getCell(c, r)

        c = PLAY_NAME_POSITION + self.play_count + 1
        r = NEW_PEOPLE_POSITION + self.people_count - 1
        end = getCell(c, r)

        self.sheet.range(start, end).clear_contents()

    def copyName(self):
        for i in range(self.people_count):
            source = getCell(PLAY_NAME_POSITION, OLD_PEOPLE_POSITION + i)
            target = getCell(PLAY_NAME_POSITION, NEW_PEOPLE_POSITION + i)
            self.sheet[target].value = self.sheet[source].value


    def calcWinner(self):
        for i in range(self.play_count):
            self.setMax(PLAY_NAME_POSITION + i + 1)

    def sumWinner(self):
        for i in range(self.people_count):
            start = getCell(PLAY_NAME_POSITION + 1, NEW_PEOPLE_POSITION + i)
            end = getCell(PLAY_NAME_POSITION + self.play_count, NEW_PEOPLE_POSITION + i)
            target = getCell(PLAY_NAME_POSITION + self.play_count + 1, NEW_PEOPLE_POSITION + i)

            # sum the big winner
            sum_string = '=SUM({:s}:{:s})'.format(start, end)
            self.sheet[target].value = sum_string

            # copy the big winner
            winner = getCell(PLAY_NAME_POSITION + self.play_count + 2, OLD_PEOPLE_POSITION + i)
            self.sheet[winner].value = self.sheet[target].value


    def setMax(self, column):
        index = 0
        max = 0
        for i in range(self.people_count):
            pos = getCell(column, OLD_PEOPLE_POSITION + i)
            if self.sheet[pos].value is not None:
                if self.sheet[pos].value > max:
                    max = self.sheet[pos].value
                    index = i
                elif self.sheet[pos].value == max:
                    pos_sum_index = getCell(PLAY_NAME_POSITION + self.play_count + 1, OLD_PEOPLE_POSITION + index)
                    pos_sum_i = getCell(PLAY_NAME_POSITION + self.play_count + 1, OLD_PEOPLE_POSITION + i)
                    if self.sheet[pos_sum_i].value > self.sheet[pos_sum_index].value:
                        index = i

        # set the big winner to 1
        pos = getCell(column, NEW_PEOPLE_POSITION + index)
        self.sheet[pos].value = 1




# convert cell coordinate to position
# (2, 3) -> 'B3'
def getCell(column, row):
    pos_c = getColumnChar(column)
    pos_r = getRowChar(row)
    position = pos_c + pos_r
    return position

# convert column number to string
# (1) -> 'A'
def getColumnChar(column):
    result = ''
    if column > 26:
        result = 'A' + chr(ord('A') + column - 27)
    else:
        result = chr(ord('A') + column - 1)
    return result

# convert row number to string
# (1) -> '1'
def getRowChar(row):
    return str(row)


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
