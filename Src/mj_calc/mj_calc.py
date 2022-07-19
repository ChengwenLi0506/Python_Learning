import xlwings as xw


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    if sheet["B1"].value == "Hello xlwings!":
        sheet["B1"].value = "Bye xlwings!"
        sheet["B1"].font.color = 255;
    else:
        sheet["B1"].value = "Hello xlwings!"
        sheet["B1"].font.color = 0;


@xw.func
def hello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    xw.Book("mj_calc.xlsm").set_mock_caller()
    main()
