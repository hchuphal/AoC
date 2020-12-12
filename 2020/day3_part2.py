def main():
    print "Elements in each row", width, total
    #x_axis = 3
    #y_axis = 1  # right 3 and down 1
    #print slope(3,1)
    #print slope(1,1)
    #print slope(5,1)
    print "Total Tress Multiplication ##", slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2)


def check_for_tree(x, y):
    x = x % width
    if raw[y][x] == "#":
        return True

def slope(x_axis, y_axis):
    x = y = 0
    total_trees = 0
    while y < total:
        if check_for_tree(x , y):
            total_trees += 1
        x += x_axis 
        y += y_axis 
    return total_trees


if __name__== "__main__":
    f= open("day3_data.txt","r") 
    if f.mode == 'r':  
        data =f.read()
    raw = data.split("\n")
    width, total = len(raw[0]), len(raw)
    main()