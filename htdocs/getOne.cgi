#!/usr/bin/perl -Tw

use strict;
use CGI;
use DBI;
use Cache::Memcached;

my($cgi) = new CGI;
print $cgi->header;
print $cgi->start_html(-title => uc("Get one Data")); #添加内容到html的title标签
print $cgi->h1("Get one Data:");
#从前台页面接受id参数
my($key) = $cgi->param('id') if defined $cgi->param('id');
#如果id为空，则提示用户输入id
if ($key eq ""){ print $cgi->h1("Please input id"); }
#连接到Memcached服务器，指定ip和端口号
my($memcached) = Cache::Memcached->new({
    servers => ["127.0.0.1:11211"],
    compress_threshold => 10_000
});

#定义数据的有效期
my($expires) = 3600; # 1 hour
#首先从Memcached中获取用户所需数据
my($value) = $memcached->get($key);
if(defined($value)){ #如果从Memcached中获取到了该数据，则说明在缓存中命中
	print $cgi->h1("Hited in the Memcached:");
    print $cgi->h3($value);
}else{ #如果未在Memcached中命中，则查询数据库，并将查询到的数据添加到Memcached中。
    my($host) = "localhost";         # 主机地址
	my($driver) = "mysql";           # 接口类型 默认为 localhost
	my($database) = "Demo";        # 数据库
	# 驱动程序对象的句柄
	my($dsn) = "DBI:$driver:database=$database:$host";  
	my($userid) = "root";            # 数据库用户名
	my($password) = "123456.";        # 数据库密码

	my($dbh) = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr; #连接数据库
	my($sth) = $dbh->prepare("SELECT * FROM user where id = $key");   # 定义待执行的SQL语句
	$sth->execute();    # 执行 SQL 操作
	while ( my(@row) = $sth->fetchrow_array() ){ #循环遍历从数据库中查询的数据结果，并显示到前台页面,并添加到Memcached中
	    print $cgi->h1("Hited in the Database:");
	    my($data) = join(' ',@row);
	    print $cgi->h3($data);
		$memcached->add($key, $data, $expires);
	}
	#关闭数据库连接，释放资源。
	$sth->finish();
	$dbh->disconnect();
}