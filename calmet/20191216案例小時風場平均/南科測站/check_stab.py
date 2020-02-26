def check_stab(Zenith_angle,cloud,ws):
    sun_tmp = 0  # 1強,2中,3弱
    stab_tmp = 0  # 1極不穩定~6極穩定
    if 35 > Zenith_angle > 0:
        if cloud == 1:
            sun_tmp = 2
        elif cloud == 0:
            sun_tmp = 1
    elif 60 > Zenith_angle > 35:
        if cloud == 1:
            sun_tmp = 3
        elif cloud == 0:
            sun_tmp = 2
    elif 90 > Zenith_angle > 60:
        if cloud == 1:
            sun_tmp = 3
        elif cloud == 0:
            sun_tmp = 3

    if Zenith_angle <= 90:
        if ws < 2:
            if sun_tmp == 1:
                stab_tmp = 1
            elif sun_tmp == 2 or sun_tmp == 3:
                stab_tmp = 2
        elif 3 > ws > 2:
            if sun_tmp == 1 or sun_tmp == 2:
                stab_tmp = 2
            elif sun_tmp == 3:
                stab_tmp = 3
        elif 5 > ws > 3:
            if sun_tmp == 1 :
                stab_tmp = 2
            elif sun_tmp == 2:
                stab_tmp = 3
            elif sun_tmp == 3:
                stab_tmp = 4
        elif 6 > ws > 5:
            if sun_tmp == 1:
                stab_tmp = 3
            elif sun_tmp == 2 or sun_tmp == 3:
                stab_tmp = 4
        elif ws > 6:
            if sun_tmp == 1:
                stab_tmp = 3
            elif sun_tmp == 2 or sun_tmp == 3:
                stab_tmp = 4
    elif  Zenith_angle > 90 :
        if ws < 2:
            stab_tmp = 6
        elif 3 > ws > 2:
            if cloud == 1 :
                stab_tmp = 5
            elif cloud == 0:
                stab_tmp = 6
        elif 5 > ws > 3:
            if cloud == 1 :
                stab_tmp = 4
            elif cloud == 0:
                stab_tmp = 5
        elif 6 > ws > 5:
            stab_tmp = 4
        elif ws > 6:
            stab_tmp = 4
    return stab_tmp    