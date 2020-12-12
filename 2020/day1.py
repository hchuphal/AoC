from itertools import *
def main():
    f= open("day1_data.txt","r") 
    if f.mode == 'r':  
        data =f.read()
    raw = data.split("\n")
    data_1 = [int(data) for data in raw]
    pairs = list(combinations(data_1, 2))
    ans_1 = list(filter(sums_2020, pairs))
    print "Combination to 2020:: ", ans_1
    product = 1
    for x in ans_1[0]:
        product *= x
    print "Product::", product

def sums_2020(values):
    return sum(values) == 2020

if __name__== "__main__":
  main()