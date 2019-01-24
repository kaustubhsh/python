<html>
<head>
<title>dbconn</title>
</head>
<h1> connecting </h1>
<?php

$username="root";
$password="redhat";
$hostname="localhost";
$dbname="adhoc";

// connecting  to database 
$dbhandle=mysql_connect($hostname,$username,$password) or die("unable to conn");

echo "connected to mysql";
$selected=mysql_select_db("$dbname",$dbhandle) or die("check database unable to connect");

$dbhandle.close();

?>


</html>
