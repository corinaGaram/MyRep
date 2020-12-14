def p1(a, b):
 while a != b:
     if a > b:
         a = a - b
     else:
         b = b - a
 return a

def p2(c):
    nr = 0
    for l in c:
        if l in ('a','e','i','o','u','A','E','I','O','U'):
            nr = nr + 1
    return nr
def p3(a,b):
   return b.count(a)

def p4(a):
    p = " "
    for c in a:
      if c.isupper() and a.index(c) !=0 :
          p = p + "_"
          p = p + c.lower()
      else:
          p = p + c.lower()
    return p

def p5():
    for i in a:
        for j in a:
            i += str(j)
    return a
if __name__ == '__main__':
   # print(p1(6,12))
   #print(p2("pisica"))
   #print(p3("ab", "abbabhsjdabb"))
   #print(p4("UpperCamelCase"))
   print(p5([[1,2,3][4,5,6][7,8,9]]))
