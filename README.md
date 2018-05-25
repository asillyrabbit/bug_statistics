## bug_statistics
Bug statistics of Zen Tao

## 实现功能
1. 对禅道上的bug进行定制化统计，生成丰富的图表报告   
![](http://p3.pstatp.com/large/pgc-image/1527232872444433daf1633)
2. 通过jenkins自动构建，每日邮件通知结果

## 准备工作
配置很简单，一次配置，长期受用。
1. 禅道上bug严重程度定义（后台->自定义->bug）   
![](http://p1.pstatp.com/large/pgc-image/15272312159912bc3ba1715)
2. 禅道上bug类型定义   
![](http://p1.pstatp.com/large/pgc-image/15272312463859815656ceb)
3. 进入“测试->bug”目录，定义提交问题的迭代、功能模块、所属端（可选）   
![](http://p3.pstatp.com/large/pgc-image/1527231642729d2b1b8d0f8)
4. 根据实际情况，修改“configuration.py”文中的配置信息   
![](http://p9.pstatp.com/large/pgc-image/15272319775518d7def9188)
5. 新建一个bat文件   
![](http://p1.pstatp.com/large/pgc-image/152723208785721e17895ee)
6. 安装jenkins
7. 构建一个自由风格的软件项目   
![](http://p1.pstatp.com/large/pgc-image/15272329044085beb2c7373)
8. 构建方式选择，windows批处理命令   
![](http://p9.pstatp.com/large/pgc-image/15272331123489e0a57cedb)
9. 先自动构建一次，生成工作空间
10. 将第5步的bat文件放到工作空间目录下   
![](http://p3.pstatp.com/large/pgc-image/1527233020627b3bf08fbbb)
11. 进行项目，“立即构建”   
![](http://p9.pstatp.com/large/pgc-image/1527233152685a513ec80fb)
12. 接收邮件，查看结果   
![](http://p3.pstatp.com/large/pgc-image/1527233335010b6f52d31e5)

## 补充说明
如果不需要jenkins，只需要配置前4步，直接执行run.py就可以生成报告
