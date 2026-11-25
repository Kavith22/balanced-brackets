from stack import stack
n=stack()
brackets='([()])'
open=['(','{','[']
close=[')','}',']']
def isbalanced(expression):
    for i in expression:
        if i in open:
            n.push(i)
        else:
            x=close.index(i)
            print(x)
            if len(n.list)>0 and open[x]==n.list[x]:
                n.pop()
    if len(n)==0:
        return 'balanced'
    else:
        return 'unbalanced'
    n.display()
print(isbalanced(brackets))