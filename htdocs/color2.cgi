#!/usr/bin/perl -Tw

use strict;
use CGI;
use DBI;
use Cache::Memcached;

my($host) = "localhost";         # 主机地址
my($driver) = "mysql";           # 接口类型 默认为 localhost
my($database) = "Demo";        # 数据库
# 驱动程序对象的句柄
my($dsn) = "DBI:$driver:database=$database:$host";  
my($userid) = "root";            # 数据库用户名
my($password) = "123456.";        # 数据库密码

my($dbh) = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr;
my($sth) = $dbh->prepare("SELECT * FROM user");   # 预处理 SQL  语句
$sth->execute();    # 执行 SQL 操作

my($cgi) = new CGI;
print $cgi->header;
my($color) = "white";
$color = $cgi->param('color') if defined $cgi->param('color');


my($key) = "foo";
my($value) = "bar";
my($expires) = 3600; # 1 hour

my($memcached) = Cache::Memcached->new({
    servers => ["127.0.0.1:11211"],
    compress_threshold => 10_000
});
$memcached->add($key, $value, $expires);
my $ret = $memcached->get($key);
print $cgi->h1($ret);

print $cgi->start_html(-title => uc($color),
                       -BGCOLOR => $color);
print $cgi->h1("This is $color");

while ( my(@row) = $sth->fetchrow_array() )
{
      print $cgi->h3(@row);
}
$sth->finish();
$dbh->disconnect();

print $cgi->end_html;
