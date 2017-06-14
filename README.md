说明： 此处提供配置好的tinyhttpd，其中包含该演示项目所涉及到的sql脚本，配置修改好的tinyhttpd(这里访问端口修改成了8888)，一个访问页面Demo.html，以及多个cgi脚本。
# 一、运行环境搭建：(具体环境搭建过程略)
## 1.编译安装tinyhttpd(可直接安装该项目提供的tinyhttpd)
## 2.安装Mysql
## 3.安装Memcached
### 3.1.安装libevent
### 3.2.安装Memcached
## 4.Perl环境配置(一般安装后系统自带Perl运行环境，若没有，则需要先安装Perl，在执行如下步骤)
### 4.1.安装perl-dbi模块(用于Perl访问MySQL数据库)
### 4.2.安装Cache::Memcached模块(用于Perl访问Memcached)
下载Cache::Memcached模块并安装(http://search.cpan.org/~dormando/Cache-Memcached-1.30/lib/Cache/Memcached.pm)                         
或者直接执行：perl -MCPAN -e 'install Cache::Memcached'(需先安装perl的cpan）
# 二、运行
## 0.执行sql脚本(tinyhttpd下的Demo.sql文件)，开启Memcached服务。
## 1.启动tinyhttpd服务器
在tinyhttpd根目录下。执行   $ ./httpd 命令
注意：若要通过局域网访问，须在防火墙中开放8888端口。
## 2.验证项目是否搭建好
打开浏览器，
如果在本地执行，则直接访问127.0.0.1:8888即可看到tinyhttpd的首页。输入颜色可以跳转到不同背景色的页面。    
如果在局域网内访问，则直接访问ip:8888即可看到tinyhttpd的首页。输入颜色可以跳转到不同背景色的页面。
## 3.访问Demo.html
打开浏览器，输入ip:8888/demo,html，接下来即可进行相应的操作。

**注意：**
cgi脚本的权限问题(最少得赋予一般用户读和执行的权限，建议0755)     
需要在cgi脚本里修改Memcached以及MySQL的相关配置(如ip地址，Mysql的密码等。)
# 三、关于3个cgi脚本
这3个cgi脚本都是使用perl语言编写，其中addOne.cgi脚本实现向数据库中添加一条记录，getAll.cgi实现了查询所有记录，getOne.cgi脚本中实现了查询一条记录，但是会优先去Memcached中查询，若Memcached中没有，则去请求数据库，并将数据添加到Memcached中。
# 参考资料
http://blog.csdn.net/u010817321/article/details/52765383  
http://blog.csdn.net/cqu20093154/article/details/41025885  
https://dev.mysql.com/doc/mysql-ha-scalability/en/ha-memcached-interfaces-perl.html  
