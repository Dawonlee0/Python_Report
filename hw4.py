# 개념 확인 과제 5.5

def rep_char(nstr):
    print('-' * nstr)

def draw_line_string(name):
    print(f'Hello {name}'.center(nstr + 4))
    print('welcom to Seoul'.center(nstr + 4))

name = input('his/her name: ')
msg1 = (f'Hello {name},')
msg2 = ('welcom to Seoul')
nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)

rep_char(nstr + 4)
draw_line_string(name)
rep_char(nstr + 4)

