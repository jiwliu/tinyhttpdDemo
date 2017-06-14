#!/usr/bin/perl -Tw

use strict;
use CGI;
use DBI;

my($cgi) = new CGI;  #定义CGI
print $cgi->header;  #使用CGI来定制html也的header部分。

my($host) = "localhost";         # 主机地址
my($driver) = "mysql";           # 接口类型 默认为 localhost
my($database) = "Demo";        # 数据库
# 驱动程序对象的句柄
my($dsn) = "DBI:$driver:database=$database:$host";  
my($userid) = "root";            # 数据库用户名
my($password) = "123456";        # 数据库密码

my($dbh) = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr; #连接数据库
my($sth) = $dbh->prepare("SELECT * FROM user");   # 定义待执行的SQL语句
$sth->execute();    # 执行 SQL 操作

print $cgi->h1("List All Data:");
print $cgi->start_html(-title => uc("getAll"));  #html的title表
                         

while ( my(@row) = $sth->fetchrow_array() ) #循环遍历从数据库中查询的数据结果，并显示到前台页面
{
    print $cgi->h3(@row);   
}
#关闭数据库连接，释放资源。
$sth->finish();
$dbh->disconnect();
#结束html的标签
print $cgi->end_html;
