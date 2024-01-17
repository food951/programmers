def solution(wallpaper):
    lux,luy,rdx,rdy=len(wallpaper),len(wallpaper[0]),0,0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j]== "#":
                if i < lux:
                    lux=i
                if j < luy:
                    luy=j
                if i> rdx:
                    rdx=i
                if j> rdy:
                    rdy=j
    return [lux,luy,rdx+1,rdy+1]