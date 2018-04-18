# selenium_module
#### 基于Selenium框架运用python语言以及unittest单元测试框架，搭建的Web端的UI自动化框架如下：
##### WebAuto/:
* config层: 存放配置文件以及测试数据，把所有的项目的配置均放在这里，用python支持较好的配置文件格式如ini等进行配置。
                       实现配置和数据与代码分离。
* driver层: 存放所需的驱动，如chromedriver、iedriverserver等。
* log层: 存放生成的日志文件，包括运行日志Runtime.log和错误日志Error.log等
* report层: 存放程序运行生成的html格式报告
* screenshot: 存放测试用到的图片以及测试时用例失败截图
* src:源码层
* common层: 框架级公用方法库
    * chche.py: 缓存
    * confparser.py: 配置文件解析器,读取配置文件数据类
    * dbsever.py: 数据库操作公用类
    * emailsever.py: 发送邮件服务封装公用类
    * initdriver.py: 初始化driver类
    * log.py: 日志记录公用类
    ...
    (如果还有框架级别的公用方法，还可以在该层封装成类，通过面向对象的方式调用即可)
  * functions层: 用例级公用方法库(元素操作公用方法封装，基于PageObject模式对控件公用方法封装，常用业务操作封装)
    * baseaction.py: 封装元素常用操作的一些公用方法
    * login.py: 登录操作
    ...
    (该层主要是封装用例层面的公用方法，常用的操作步骤，针对PageObject思想对不同类型的页面控件元素的操作封装等)
  * testcase层: 测试用例层
      * basecase.py: 测试用例基础类
      * testcase1.py: 测试用例1
        ...
      * runner层: 测试套件层,执行器，组织的测试套件suite，生成html格式测试报告
      * testrunner.py: 各种加载测试用例的方法封装，以及生成报告
* run.py: 执行器，整个框架运行该文件即可
