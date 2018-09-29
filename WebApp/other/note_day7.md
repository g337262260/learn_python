# Note7

####做项目中的一些不懂的一些东西，做一些笔记

- jinja2（https://www.cnblogs.com/dachenzi/p/8242713.html

    https://blog.csdn.net/qq_38801354/article/details/77150637）
  
  jinja2被广泛使用的优点:
  1. 相对于Template，jinja2更加灵活，它提供了控制结构，表达式和继承等。
  2. 相对于Mako，jinja2仅有控制结构，不允许在模板中编写太多的业务逻辑
  3. 相对于Django模板，jinja2性能更好。
  4. Jinja2模板的可读性很棒。
  
        > pip3 install jinja2
        
        > python -c "import jinja2"
  
  基本语法：
  1. 控制结构 {% %}
  2. 变量取值 {{ }}
    
        变量可以通过“过滤器”进行修改，过滤器可以理解为是jinja2里面的内置函数和字符串处理函数。
        
  3. 注释 {# #}
  
- Environment:

    Jinja2中的一个核心类，它的实例用来保存配置、全局对象，以及文件路径用于加载模板。
    
    配置Jinja2来为应用添加模板的步骤大致是：
    
    - 创建Environment实例
    - 使用get_template()加载模板
    - 使用render()方法来渲染模板
    
    
    

   


     







