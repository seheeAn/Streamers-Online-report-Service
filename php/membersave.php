<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<?php
include "db_conn.php";

$id=$_POST['id'];
$password=($_POST['pw']);
$name=$_POST['name'];

$sql = "insert into member ( id, pw, name)";
$sql = $sql."values('$id','$password','$name')";
if($mysqli->query($sql)){
 echo "<script>alert('{$name} 님 가입 되셨습니다.');</script>";
}else{
 echo 'fail to insert sql';
}
mysqli_close($mysqli);

echo"<script>location.href='../sign_in.html';</script>"; 

?>
</body>
</html>
