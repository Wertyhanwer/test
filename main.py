s = 5
stop = False
#a, b, c, d, e = 0,0,0,0,0

for i_a in range(1,151):
    print(i_a)
    if stop == True:
        break
    for i_b in range(i_a,151):
        for i_c in range(i_b,151):
            for i_d in range(i_c, 151):
                for i_e in range(i_d, 151):
                    #print(i_a, i_b , i_c , i_d , i_e)
                    if i_a**s + i_b**s + i_c**s + i_d**s == i_e**s:
                        print(i_a + i_b + i_c + i_d + i_e)
                        stop = True
####
###
##sdfsdfsdfsfsd