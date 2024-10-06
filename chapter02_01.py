# Chapter02-1
# 파이썬 완전 기초
# print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''python Start!''')
print("""python Start!""")


print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '7777', sep='-')
print('python', 'goole.com', sep='@')

print()

# end 옵션

print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

# file 옵션( 어떤 파일에 쓸때 씀)
import sys

print('LEarn Python', file=sys.stdout) #sys.stdout 콘솔 아웃 말함 걍 출력
print()

# format 사용(d(정수: 3), s(문자열: python), f(실수: 3.141592)) **중요
print('%s %s %s' % ('one', 'two', 'three'))
print('%d %d' % (3, 5))
print('%f %f' % (3.141592, 564.323))


print()
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

# %s
print('%10s' % ('nice12345')) #왼쪽 빈칸
print('{:>10}'.format('nice'))

print('%-10s' % ('nice12345')) #오른쪽 빈칸
print('{:10}'.format('nice'))

print('{:$>10}'.format('nice')) #왼쪽 부터 빈칸 $로 채움

print('{:^10}'.format('nice')) #중앙정렬

print('%5s' % ('nice'))
print('%.5s' % ('pythonprograming')) #왼쪽부터 5글자까지만(절삭)
print('%5s' % ('pythonprograming'))
print('{:10.5}'.format('pythonprograming')) #10개의 공간이 있고 글자를 5개로 자름



# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))

print()

# %f

print('%f' % (4.141592))
print('{:f}'.format(3.141592))
print('%6.2f' % (4.141592))
print('{:10f}'.format(3.141592))


