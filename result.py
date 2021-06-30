<?php

$yname = $_GET['yname'];
$fname = $_GET['fname'];

$per = mt_rand(90,200);

echo "<br><br><br>";
echo "<h4 align='center'>Friendship Calculator</h4><br>";
echo "<br><h2 align='center'>Friendship between ".$yname." and ".$fname." is</h2><br>";
echo "<h1 align='center'>".$per."% Strong</h1>";

?>
