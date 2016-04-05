# -* - coding: UTF-8 -* -
#!/usr/bin/python
# Filename: objvar.py

class Person:
    '''Represents a person.'''
    # 这是类的变量
    print "gexing class set"
    population = 0

    # 构造函数
    def __init__(self, name):
        '''Initializes the person's data.'''  #类的文档字符串
        import ipdb; ipdb.set_trace()
        print "gexing, init set"
        # 这里是self.name，所以这个name是对象的变量
        self.name = name
        print '(Initializing %s)' % self.name
        # 构造函数使得类的变量population+1
        Person.population += 1

    # 析构函数
    def __del__(self):
        import ipdb; ipdb.set_trace()
        '''I am dying.'''  #方法的文档字符串
        print "gexing, del set"
        print '%s says bye.' % self.name
        Person.population -= 1

        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.' % Person.population

    def sayHi(self):
        import ipdb; ipdb.set_trace()
        '''Greeting by the person.

        Really, that's all it does.'''
        print 'Hi, my name is %s.' % self.name

    def howMany(self):#如果这个函数要调用本类的sayHi(self),需要操作self.sayHi()
        import ipdb; ipdb.set_trace()
        '''Prints the current population.'''
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d persons here.' % Person.population

# 我们可以在运行时使用Person.__doc__和Person.sayHi.__doc__来分别访问类与方法的文档字符串。
import ipdb; ipdb.set_trace()
swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()
