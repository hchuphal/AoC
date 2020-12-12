def main():
    f= open("day2_data.txt","r") 
    if f.mode == 'r':  
        data =f.read()
    raw = data.split("\n")
    # policies
    p_and_p = [password_dict(passwords) for passwords in raw]
    valid_data = list(filter(valid_passwords_2, p_and_p))
    print "Total Valid passwords::", len(valid_data)

def password_dict(password):
    pass_dict = {} #empty
    #regex 13-14 f: ffffffffnfffvv
    split_password = password.split() # by space
    pass_range = split_password[0].split("-") # atleasr and atmost
    pass_dict["lower"] = int(pass_range[0])
    pass_dict["upper"] = int(pass_range[1])
    pass_dict["letter"] = split_password[1][0]
    pass_dict["pass"] = split_password[2]
    return pass_dict 

def valid_passwords_2(password):
    lower = password["lower"]
    upper = password["upper"]
    pos_1 = password["pass"][lower - 1] == password["letter"]
    pos_2 = password["pass"][upper - 1] == password["letter"]
    verdict = (pos_1 ^ pos_2)
    return verdict


if __name__== "__main__":
  main()