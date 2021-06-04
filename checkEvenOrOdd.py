import sys
import random
def makeFile(min, max):
    f = open('temp.py', 'w')
    f.write('def main(val):\n\tif(val == ' + str(min) + ') :\n')
    if min % 2 == 0:
        f.write('''\t\tprint('Even')\n''')
    else:
        f.write('''\t\tprint('Odd')\n''')
    for i in range(min + 1, max + 1):
        f.write('\telif(val == ' + str(i) + '):\n')
        if i % 2 == 0:
            f.write('''\t\tprint('Even')\n''')
            continue
        f.write('''\t\tprint('Odd')\n''')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: ' + sys.argv[0] + ' <value to check>')
    elif len(sys.argv) == 2:
        makeFile(int(sys.argv[1]) - 10, int(sys.argv[1]) + 10)
        if random.randint(int(sys.argv[1]) - 3, int(sys.argv[1]) + 3) == int(sys.argv[1]):
            import temp
            temp.main(int(sys.argv[1]))
        else:
            print('I dont know, try again?')
