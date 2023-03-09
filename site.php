<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>		

		
		<?php
		
			function find_sum($k, $max_sum, $ls, $t){
				if($k == 0){
					//print_r($ls); echo " summa = $max_sum <br>";
					return $max_sum;
				}
				$summ = $max_sum;
				for($i=0;$i<=count($ls)-$k;$i++){
					$summ1 = find_sum($k-1, $max_sum + $ls[$i], array_slice($ls, $i+1), $t);
					if($summ1 > $summ && $summ1 <= $t){
						$summ = $summ1;
					}
				}
				return $summ;
			}
		
			function chooseBestSum($t, $k, $ls) {
				
				echo "t:"; print_r($t); echo "<br>";
				echo "k:"; print_r($k); echo "<br>";
				echo "list:"; print_r($ls); echo "<br>";
				
				if($t<3){
					return null;
				}
				$list = $ls;
				sort($list);
				//print_r($list);
				$su=0;
				for($i=0; $i<$k; $i++){
					$su += $list[$i];
				}
				if($su > $t){
					return null;
				}
				$lenght = count($list);
				//$i = $lenght;
				$max_sum = find_sum($k,0,$ls,$t);
				
				/*
				for($i=0;$i<$lenght-2;$i++){
					for($j=$i+1;$z<$lenght-1;$j++){
						for($z=$j+1;$z<$lenght;$z++){
							
							$summ = $ls[$i]+$ls[$j]+$ls[$z];
							if($summ == $t){
								return $summ;
							}elseif($summ > $max_sum && $summ < $t){
								$max_sum = $summ;
							}
						}
						
					}
				}*/
				return $max_sum;
			}
			
			//$ts = [50, 55, 56, 57, 58];
			//echo chooseBestSum(163, 3, $ts);
			
			//$ts = [91, 74, 73, 85, 73, 81, 87];
			//echo chooseBestSum(230, 3, $ts);
			
			//$ts = [91, 74, 73, 85, 73, 81, 87];
			//echo chooseBestSum(331, 5, $ts);
			$ts = [50];
			echo chooseBestSum(163, 3, $ts);

		?>
		
		
		<form action="site.php" method="post">
			
			<input type="submit">
		</form>

		
		
	</body>


</html>
