<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
		
		
		
		<form action="site.php" method="post">
			Male?:<input type="checkbox" name="male">
			Short?:<input type="checkbox" name="short">
			
			<input type="submit">
		</form>
		
		
		
		<?php 			
			function sayHi($name2, $age2){
				echo "Hello, $name2, aged $age2";
			}
			function cube($num){
				return $num * $num * $num;
			}
			
			$name = "George";
			$age = 43;
			sayHi($name, 43);
			echo "<br/>";
			sayHi("Karen", cube(4));
			echo "<br/>";
			
			$isMale = $_POST["male"];
			$isTall = $_POST["short"];
			if ($isMale && !$isTall){
				echo "You are a tall male";
			} elseif ($isMale || $isTall){
				echo "You are either male or short";
			} else {
				echo "You are neither male nor short";
			}
			

		?>
		
		
		
	</body>


</html>
