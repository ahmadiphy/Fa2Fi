from Fa2Fi_dicts import *


def return_Fi(Fa_str):
    Fi_str= ''
    #
    if Fa2Fi_dict.get(FA_str[0], None) != None:
        Fi_str = Fi_str + Fa2Fi_dict_UP[Fa_str[0]]
    else:
        Fi_str = Fi_str + Fa_str[0]
    #
    for i in range(1, len(Fa_str)):
        if Fa2Fi_dict.get(FA_str[i], None) != None:
            Fi_str = Fi_str + Fa2Fi_dict[Fa_str[i]]
        else:
            Fi_str = Fi_str + Fa_str[i]
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