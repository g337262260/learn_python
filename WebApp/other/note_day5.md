# Note5

####做项目中的一些不懂的一些东西，做一些笔记

- functools.wraps装饰器模块
   1. 被装饰的函数不受装饰器的影响
   2. 装饰器的名字变成被装饰的名字，外部调用到的被装饰函数的功能
   3. 把原函数的name等属性复制到wrapper函数中。
- @staticmethod与@classmethod的区别
   一般来说，要使用某个类的方法，需要先实例化一个对象再调用方法。 
而使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。 
这有利于组织代码，把某些应该属于某个类的函数给放到那个类里去，同时有利于命名空间的整洁。
   
   - @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
   - @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
   
   如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。 
而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。
    ```
    [python] view plain copy
    class A(object):  
    bar = 1  
    def foo(self):  
        print 'foo'  

    @staticmethod  
    def static_foo():  
        print 'static_foo'  
        print A.bar  

    @classmethod  
    def class_foo(cls):     #这里用了cls参数，即A这个类本身，后面要使用类.属性或类.方法时就可以用cls.属性或cls.方法，避免硬编码
        print 'class_foo'  
        print cls.bar  
        cls().foo()     #类.方法的调用，没有使用类的名字(A)，避免硬编码

    A.static_foo()  
    A.class_foo()  
    输出
    static_foo
    1
    class_foo
    1
    foo
    ```
-  关于python中inspect模块的一些探究
   
   inspect模块主要提供了四处用处
   1. 对事都是模块、框架、函数等进行类型检查
   2. 获取源码
   3. 获取类或者函数的参数信息
   4. 解析堆栈
   
   今天用到的为第三种用处，即获取类或者函数的参数信息
   
   - inspect.signature（fn)将返回一个inspect.Signature类型的对象，值为fn这个函数的所有参数
   - inspect.Signature对象的paramerters属性是一个mappingproxy（映射）类型的对象，值为一个有序字典（Orderdict)。
   
        - 这个字典里的key是即为参数名，str类型
        - 这个字典里的value是一个inspect.Parameter类型的对象，根据我的理解，这个对象里包含的一个参数的各种信息
  
   - inspect.Parameter对象的kind属性是一个_ParameterKind枚举类型的对象，值为这个参数的类型（可变参数，关键词参数，etc）
   - inspect.Parameter对象的default属性：如果这个参数有默认值，即返回这个默认值，如果没有，返回一个inspect._empty类。
   
   inspect.Parameter的几种参数类型
   
   - POSITIONAL_ONLY：位置参数
   - VAR_POSITIONAL：可变参数
   - KEYWORD_ONLY：命名关键字参数
   - VAR_KEYWORD：关键字参数
   - POSITIONAL_OR_KEYWORD：位置参数或命名关键字参数
   
- python _、__和__xx__的区别

    默认情况下，Python中的成员函数和成员变量都是公开的(public),在python中没有类public,private等关键词来修饰成员函数和成员变量。其实，Python并没有真正的私有化支持，但可用下划线得到伪私有。   尽量避免定义以下划线开头的变量！
    
    - "_"单下划线  :Python中不存在真正的私有方法。为了实现类似于c++中私有方法，可以在类的方法或属性前加一个“_”单下划线，意味着该方法或属性不应该去调用，它并不属于API。
        Python中没有真正的私有属性或方法,可以在你想声明为私有的方法和属性前加上单下划线,以提示该属性和方法不应在外部调用.如果真的调用了也不会出错,但不符合规范.
        ```
            #!/usr/bin/env python
            # coding:utf-8
            class Test():
            def __init__(self):
                pass
            def _one_underline(self):  # 定义私有方法，都只能被类中的函数调用，不能在类外单独调用
                print "_one_underline"
            def __two_underline(self): # 防止类被覆盖，都只能被类中的函数调用，不能在类外单独调用
                print "__two_underline"
 
            def output(self):
                self._one_underline()
                self.__two_underline()
            if __name__ == "__main__":
 
            obj_test=Test()
            obj_test.output()

            #输出结果为：
            localhost:attempt_underline a6$ python undeline.py
            _one_underline
            __two_underline
    - "__"双下划线 : 它并不是用来标识一个方法或属性是私有的，真正作用是用来避免子类覆盖其内容。
      因此，在我们创建一个以"__"两个下划线开始的方法时，这意味着这个方法不能被重写，它只允许在该类的内部中使用。  
        ```
        #!/usr/bin/env python
        # coding:utf-8
        class A(object):
            def __method(self):
                print "I'm a method in A"
            def method(self):
                self.__method()
        
        class B(A):
            def __method(self):
                print "I'm a method in B"
 
        if __name__ == "__main__":
            a = A()
            a.method()
            b = B()
            b.method()
        # 输出结果为：
        localhost:attempt_underline a6$ python undeline.py
        I'm a method in A
        I'm a method in A
    - "__xx__"前后各双下划线 : “__xx__”经常是操作符或本地函数调用的magic methods。在上面的例子中，提供了一种重写类的操作符的功能。
        在特殊的情况下，它只是python调用的hook。例如，__init__()函数是当对象被创建初始化时调用的;__new__()是用来创建实例。
    
    结论
    使用_one_underline来表示该方法或属性是私有的，不属于API；
    当创建一个用于python调用或一些特殊情况，如子类不能覆盖的那些父类方法时，使用__two_underline__；
    使用__just_to_underlines，来避免子类的重写！
       

        

   


     







