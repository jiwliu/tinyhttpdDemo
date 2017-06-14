#!/usr/bin/perl -Tw

use strict;
use CGI;
use DBI;

my($cgi) = new CGI;

print $cgi->header;
print $cgi->start_html(-title => uc("Add one Data")); #添加内容到html的title标签
#输出提示信息到页面
print $cgi->h1("Add one Data:");
#接受网页传来的参数，并赋值给相应变量
my($username) = $cgi->param('username') if defined $cgi->param('username');
my($password) = $cgi->param('password') if defined $cgi->param('password');
my($salt) = $cgi->param('salt') if defined $cgi->param('salt');
my($headurl) = $cgi->param('headurl') if defined $cgi->param('headurl');
#输出用户的参数信息到页面
print $cgi->h3("username = $username");
print $cgi->h3("password = $password");
print $cgi->h3("salt = $salt");
print $cgi->h3("headurl = $headurl");
#定义连接数据库所需变量
my($host) = "localhost";         # 主机地址
my($driver) = "mysql";           # 接口类型 默认为 localhost
my($database) = "Demo";        # 数据库
# 驱动程序对象的句柄
my($dsn) = "DBI:$driver:database=$database:$host";  
my($userid) = "root";            # 数据库用户名
my($password) = "123456";        # 数据库密码
my($dbh) = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr;
# 预定义 SQL  语句
my $sth = $dbh->prepare("INSERT INTO user
                       (username, password, salt, head_url)
                        values
                       ('$username', '$password', '$salt', '$headurl')");
$sth->execute() or die $DBI::errstr; #执行SQL语句，执行结果保存在sth变量中

print $cgi->h1("Finished!");
#关闭连接释放资源。
$sth->finish();
$dbh->disconnect();
#结束html页面
print $cgi->end_html;
