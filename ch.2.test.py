print('Welcome to', end='         ')
print('IT NEWS', end='')
print('Web Site')


import sys
print('sys가 뭐임 썅 왜 되다가 안되다가 악!!', file=sys.stdout)

# format (d, ->  정수 s, f)
print()
print('%s %s'% ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('안녀아', '하세요'))

print()
print('%10s' % ('nicenive'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nicenive'))
print('{:10}'.format('nice'))


print('{::>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('{:>10.5}'.format('nicesydy'))
print('%10.5s' % ('niceover') )



print('%d %d' % (1, 2))

print('{} {}'.format('1', '2'))



print()
print('%10d' % (12))
print('{:4d}'.format(12))
print('{:10}'.format('nice'))
print('%10s' % ('nice'))
 


print('%06.2f' % (4.141592))
print('{:10f}'.format(3.141592))