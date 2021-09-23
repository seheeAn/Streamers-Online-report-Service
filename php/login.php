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

if($id == "" || $password == ""){
	echo "<script> alert('아이디 혹은 패스워드를 입력하세요'); history.back(); </script>";
}

$sql = "select id, pw, name from member where member.id='".$id."'";
$data = mysqli_query($mysqli, $sql);
$guest = $data->fetch_array();


if($guest['id'] == $id && $guest['pw'] == $password && $guest['id'] != ""){

	session_start();
	 $_SESSION['user_id']=$id;
	 $_SESSION['user_name']=$guest['name'];
	echo "<script>alert('로그인되었습니다.');
	location.href='../main_page.php';</script>";


}else{
	echo "<script>alert('아이디 혹은 비밀번호를 확인하세요.'); history.back();</script>";
}

mysqli_close($mysqli);

?>
</body>
</html>
