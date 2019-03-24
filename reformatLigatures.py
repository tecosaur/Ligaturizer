import ligatures

ligs = ligatures.ligatures[:]

for lig in ligs:
    lig['chars'] = [y for x in list(map(lambda char: [char] if type(char).__name__ == 'int' else list(char), lig['chars'])) for y in x]

import operator

ligs.sort(key=operator.itemgetter('chars'))

open('ligatures.py', 'w').write('''

ligatures = {}

'''.format(str(ligs).replace('}, {', '},\n\t{')))
