def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i < x:
            print("{}".format(my_list[i]), end="")
            i += 1
        print("")
        return i
    except:
        print("")
        return i