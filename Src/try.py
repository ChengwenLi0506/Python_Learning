import xlwings as xw

app = xw.apps.active
book1 = app.books.active
sheet1 = book1.sheets[0]

cells = sheet1.range('A1', 'H15')
cells.value = 456
