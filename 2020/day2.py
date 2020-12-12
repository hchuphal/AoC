def main():
    f= open("day2_data.txt","r") 
    if f.mode == 'r':  
        data =f.read()
    raw = data.split("\n")
    # policies
    p_and_p = [password_dict(passwords) for passwords in raw]
    valid_data = list(filter(check_valid_password, p_and_p))
    print "Total Valid passwords::", len(valid_data)

def password_dict(password):
    pass_dict = {} #empty
    #regex 13-14 f: ffffffffnfffvv
    split_password = password.split() # by space
    pass_range = split_password[0].split("-") # atleasr and atmost
    pass_dict["lower"] = int(pass_range[0])
    pass_dict["upper"] = int(pass_range[1])
    pass_dict["letter"] = split_password[1][0] #remove :
    pass_dict["pass"] = split_password[2]
    return pass_dict 

def check_valid_password(passwords):
    total_letters = passwords["pass"].count(passwords["letter"])
    total = passwords["lower"] <= total_letters <= passwords["upper"] # using regex
    return total


if __name__== "__main__":
  main()