new_row = [1,1]
def make_new_row(new_row):
    x = new_row[0]+ new_row[1]
    new_row.insert(1,x)
    return new_row

row = make_new_row(new_row)

print(row)