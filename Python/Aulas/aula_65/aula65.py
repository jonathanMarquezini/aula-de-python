def soma(x, y, z=None):
    # if z:
    #     print(f'{x=} + {y=} + {z=} = {x + y + z}')
    # elif x == 0 and y == 0 and z == 0:
    #     print('Campos vazios')
    # else:
    #     print(f'{x=} + {y=} = {x + y}')

    if z is not None:
        print(f'{x=} + {y=} + {z=} = {x + y + z}')
    else:
        print(f'{x=} + {y=} = {x + y}')

soma(1, 2)
soma(1, 2, 3)