speed=40
is_birthday=True
if speed < 31:
    print('no ticket')
elif speed > 30 and speed <51:
    if is_birthday:
        if speed<50+5:
            print('no ticket')
        else:
            print('small ticket')
    else:
        print('small ticket')
elif speed > 50:
    if is_birthday:
        if speed<=50+5:
            print('no ticket')
        else:
            print('big ticket')
    else:
        print('big ticket')
        
        
