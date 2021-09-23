<!DOCTYPE html>
<?php session_start(); ?>
<html>
<head>
<meta charset="UTF-8">
<title>SOS</title>
<link rel="stylesheet" href="../css/style.css?2">
</head>
<body>
	<div class="container">
	<header>
			<h1><a href="../main_page.php"><img src="../images/logo.png" width="456" height="190"></a></h1>
			<nav>
				<ul class = "userMenu">
					<?php
					if(!isset($_SESSION['user_id']) || !isset($_SESSION['user_name'])) {
						echo "<li><a href='../sign_in.html'>SIGN IN &nbsp;&nbsp;</a></li>";
						echo "<li><a href='../sign_up.html'>SIGN UP &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>";
					} else {
						$user_id = $_SESSION['user_id'];
						$user_name = $_SESSION['user_name'];
						echo "<li><a href=''>Welcome $user_id</a></li>";
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
	<h1><b>Basic</h1>
	<p>anyone wants to experience</p>
	<h2> For Free </h2>
	<h1><b>Amateur</h1>
	<p> for non-professional editor and streamer</p>
	<h2> 49$ / month </h2>
	<h1><b>Pro</h1>
	<p> for professional editor and streamer</p>
	<h2> 99$ / month </h2>
	</div>

	<div class="multi3">
	<br>
	<p><ins>3 chances</ins> for Highlight analysis</p>
	<p>Free Community</p>
	<p><del>Keyword Collection</del></p>
	<p><del>Searching for Chat</del></p>
	<p><del>Extracting Chat</del></p>

	<br>
	<p><ins>10 times</ins> a month</p>
	<p>Free Community</p>
	<p>Keyword Collection</p>
	<p>Searching for Chat</p>
	<p>Extracting Chat</p>

	<br>
	<p><ins>Unlimited</ins></p>
	<p>Free Community</p>
	<p>Keyword Collection</p>
	<p>Searching for Chat</p>
	<p>Extracting Chat</p>


	</div>
	</section>
	<div class="multi2"><div class="main-form2">
		<br>
		<br>
	<p><center>
   		<button onclick="location.href='file_list_private.php'">3 chances left</button></p>
		<p>
		</center>
		<center>
			<br>
			<br>
   		<button onclick="location.href='file_list_private.php'">Buy Now !</button></p>
		</center>
		<center>
			<br>
			<br>
   		<button onclick="location.href='file_list_private.php'">Buy Now !</button></p>
		</center>
		</div>

	</div>
</body>
</html>
