def return_fing(mytxt):
    mydict={'ا':'a', 'آ':'A', 'ب':'b', 'چ':'ch', 'د':'d',
                    'ف':'f', 'گ':'g', 'ح':'h', 'ی':'y', 'ج':'j',
                    'ژ':'j', 'ک':'k', 'خ':'kh', 'ل':'l', 'م':'m',
                    'ن':'n', 'پ':'p', 'ق':'gh', 'ر':'r', 'س':'s',
                    'ش':'sh', 'ت':'t', 'و':'v', 'ز':'z', 'غ':'gh',
                    'ع':'a', 'ه':'h', 'ط':'t', 'ص':'s', 'ث':'s',
                    'ظ':'z', 'ض':'z', 'ذ':'z', ' ':'', '-':''}
    text= ''
    for i in range(len(mytxt)):
        if mydict.get(mytxt[i], None) != None:
            text = text + mydict[mytxt[i]]
        else:
            text = text + mytxt[i]
    return str(text)
