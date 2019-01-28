def foo ():
    print ('runing foo')
    bar ()
def bar ():
    print ('runing bar')
    foo ()
bar()