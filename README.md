# web端UI自动化

（1）config：存放浏览器类型，url等

（2）framework：通用方法的封装

定义一个页面基类。让所有页面都继承这个类，封装一些常用的页面操作方法到这个类，如退出,关闭，打开页面元素查找等，base_page.py

浏览器相关操作的封装，browser_engine.py

（3）pageobjects：封装页面元素和行为；

（4）testsuits：测试case组件存放；

（5）tools：存放浏览器驱动；

（6）logs：存放测试完成之后生成的日志文件，可以查看日志定位问题；

（7）test_report：存放测试运行之后生成的测试报告，可以查看报告定位问题；

（8）screenshots：存放测试运行之后生成的测试截图，可以查看截图定位问题；
