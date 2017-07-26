strawberries=50
is_weekend=True
if strawberries>39 and strawberries<61:
    if is_weekend:
        print('Not Fun!')
    else:
        print('Fun')
elif strawberries>39:
    if not is_weekend:
        print('Not Fun!')
    else:
        print('Fun')


