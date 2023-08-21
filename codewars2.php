<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>
	
	
	<?php 
	for($i = 0; $i < 10; $i++){
			if($i % 2 != 0){
				#echo "$i ";
			}
			
		}
	function productFib(int $prod) {
		$first = 1;
		$second = 1;
		while($first * $second < $prod){
			$third = $first + $second;
			$first = $second;
			$second = $third;
			///echo "$second   ";
			
		}
		return (($first * $second == $prod) ? (array($first, $second, true)) : (array($first, $second, false)));
	}
	
	#print_r(10);
	$arr = productFib(4895);
	echo "$arr[0] $arr[1] $arr[2]";
	
	
	?>
	
	</body>
</html>
	