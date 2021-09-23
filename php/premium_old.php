<!DOCTYPE html>
<?php session_start(); ?>
<html>
<head>
<meta charset="UTF-8">
<title>SOS</title>
<link rel="stylesheet" href="../css/style_old.css">
</head>
<body>
	<div class="container">
	<header>
			<h1><a href="../main_page.php"><img src="../images/logo.png" width="456" height="190"></a></h1>
			<nav>
					 <ul class = "userMenu">
						 <?php
						 if(!isset($_SESSION['user_id']) || !isset($_SESSION['user_name'])) {
							 echo "<li><a href='sign_in.html'>SIGN IN</a></li>";
							 echo "<li><a href='sign_up.html'>SIGN UP &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>";
						 } else {
							 $user_id = $_SESSION['user_id'];
							 $user_name = $_SESSION['user_name'];
							 echo "<li><a href=''>$user_id 님</a></li>";
							 echo "<li><a href='sign_out.php'>SIGN OUT</a></li>";
						 }
						 ?>
					 </ul>

					 <ul class = "mainMenu">
							<li><a href="../main_page.php">Video Report</a></li>
							<li><a href="premium.php">Premium</a></li>
							<li><a href="">Community</a></li>
					</ul>
			</nav>
	</header>
	</div>
		<br>
		<br>
		<section class="NAS">
			<center><h1> Premium Pass </h1>
				<hr width="300" color="#053366">
				<div class="multi">
					<h1><b>Free</h1>

						<h2> 0$ / month </h2>
						<h1><b>Basic</h1>
						<h2> 10$ / month </h2>
						<h1><b>Premium</h1>
							<h2> 20$ / month</h2>
						</div>
					</section>
					<div class="multi2"><div class="main-form2">
						<h1><button onclick="location.href='file_list_private.php'">Buy Now</button></h1>
						<h1><button onclick="location.href='file_list_private.php'">Buy Now</button></h1>
						<h1><button onclick="location.href='file_list_private.php'">Buy Now</button></h1>
					</div>
				</div>
</body>
</html>
