from Fa2Fi_dicts import *

def check_up(c):
    state = False
    test_str = '123456789/*-+ !@#$%^&*()_[]?><.,;:'
    for i in range(len(test_str)):
        if c == test_str[i]:
            state = True
            break
    return state

def return_FaCh(c):
    result = c
    if Fa2Fi_dict.get(c, None) != None:
        result = Fa2Fi_dict[c]
    return result

def return_FaCh_UP(c):
    result = c
    if Fa2Fi_dict_UP.get(c, None) != None:
        result = Fa2Fi_dict_UP[c]
    return result

def return_Fi(Fa_str):
    Fi_str= ''
    #
    Fi_str = Fi_str + return_FaCh_UP(Fa_str[0])
    #
    for i in range(1, len(Fa_str)):
        if check_up(FA_str[i]):
            Fi_str = Fi_str + return_FaCh_UP(Fa_str[i])
        else:
            Fi_str = Fi_str + return_FaCh(Fa_str[i])
    return str(Fi_str)
    
def Final_Correction(Fi_str):
    Normal_Chars = '0123456789abcdefghijklmnopqrstuvwxyz -_=+/ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()[]"?.,~'
    for i in range(len(Fi_str)):
        this_char = Fi_str[i]
        this_char_state = False
        for j in range(len(Normal_Chars)):
            if this_char == Normal_Chars[j]:
                this_char_state = True
        if this_char_state is False:
            Fi_str[i] = '-'
    return Fi_str