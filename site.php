<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>		

		
		<?php
		
			function find_sum1($k, $max_sum, $ls, $t,$true_sum, $max_k){
				if($k == 0){
					//print_r($ls); echo " summa = $max_sum <br>";
					return [$max_sum, $true_sum];
				}
				$summ = $max_sum[0];
				//$summ2 = $max_sum[1];
				for($i=0;$i<=count($ls)-$k;$i++){
					/*$summ1 = find_sum($k-1, $max_sum + $ls[$i], array_slice($ls, $i+1), $t, $true_sum, $max_k);
					if($summ1[0] > $summ && $summ1[0] <= $t){
						print_r($ls[$i]); echo "<br>";
						$summ = $summ1[0];
						if($k == $max_k && $summ > $true_sum){
						$true_sum = $summ;
						}
					}**/
					$summ1 = find_sum($k-1, $max_sum, array_slice($ls, $i+1), $t, $true_sum, $max_k);
					if($summ1[0] + $ls[$i] > $summ && $summ1[0] + $ls[$i] <= $t){
						print_r($ls[$i]); echo "<br>";
						$summ = $summ1[0]+$ls[$i];
						if($k == $max_k && $summ1[0]+ $ls[$i] > $true_sum){
							$true_sum = $summ1[0]+ $ls[$i];
						}
					}
					/*
					$summ1 = find_sum($k-1, [$summ + $ls[$i], $max_sum[1]+1], array_slice($ls, $i+1), $t, $true_sum, $max_k);
					if($summ1[0][0] > $summ && $summ1[0][0] <= $t){
						print_r($ls[$i]); echo "<br>";
						$summ = $summ1[0][0];
						$summ2 = $summ1[0][1];
						if($summ > $true_sum && $summ1[0][1] == $max_k){
							$true_sum = $summ;
						}
					}*/

				}
				//return [[$summ,$summ2], $true_sum];
				return [$summ, $true_sum];
			}
			
			
			function find_sum2($k, $max_sum, $ls, $t,$true_sum, $max_k){
				if($k == 0){
					if($max_sum<=$t && $max_sum>$true_sum){
						return [$max_sum, $true_sum];
						//
					}elseif($max_sum<=$t){
						return [$max_sum, $true_sum];
					}else {
						return [0, $true_sum];
					}
					
				}
				$summ = $max_sum;

				for($i=0;$i<=count($ls)-$k;$i++){

					$summ1 = find_sum($k-1, $max_sum + $ls[$i], array_slice($ls, $i+1), $t, $true_sum, $max_k);
					
					if($summ1[0]>$true_sum && $k == $max_k){
						$true_sum=$summ1[0];
					}
					
					//if($summ1[0]>$summ && $summ1[0]<= $t){
						//print_r($ls[$i]); echo "<br>";
					//	$summ = $summ1[0];
					//}


				}
				//return [[$summ,$summ2], $true_sum];
				return [$summ, $true_sum];
			}
		
			function chooseBestSum2($t, $k, $ls) {
				
				echo "t:"; print_r($t); echo "<br>";
				echo "k:"; print_r($k); echo "<br>";
				echo "list:"; print_r($ls); echo "<br>";
				
				$lenght = count($ls);
				if($k>count($ls)){
					return null;
				}
				if($t<3){
					return null;
				}
				$list = $ls;
				sort($list);
				print_r($list);
				$su=0;
				for($i=0; $i<$k; $i++){
					$su += $list[$i];
				}
				if($su > $t){
					return null;
				}
				/*
				for($i=$length; $i>$k; $i--){
					$ksum = $list[$i];
					for($j=0; $j<$k-1; $j++){
						$ksum += $list[$j];
					}
					if($ksum>$t && $list[$i] != $t+1){
						$element = array_search($ls, $list[i]);
						while($element != false){
							$ls[$element] = $t + 1;
							$element = array_search($ls, $list[i]);
						}
						
					}
				}*/
				$lenght = count($list);
				//$i = $lenght;
				$max_sum = find_sum($k-1,0,$ls,$t,0, $k-1);
				
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
				echo "<br>";
				echo "<br>";
				return $max_sum[1];
			}
			
			
			
			
			
			function find_sum($k, $max_sum, $ls, $t,$true_sum, $max_k){
				if($k == 0){
					if($t<0){
						return 0;
						//
					}else{
						//if($true_sum<$max_sum){
							//return 
						//}
						//return $max_sum;
					}
					
				}
				$summ = $max_sum;

				for($i=0;$i<=count($ls)-$k;$i++){

					$summ1 = find_sum($k-1, $max_sum, array_slice($ls, $i+1), $t - $ls[$i], $true_sum, $max_k);
					
					if($summ1>$summ && $k == $max_k){
						$summ=$summ1;
					}
					
					//if($summ1[0]>$summ && $summ1[0]<= $t){
						//print_r($ls[$i]); echo "<br>";
					//	$summ = $summ1[0];
					//}


				}
				//return [[$summ,$summ2], $true_sum];
				return $summ;
			}
			
			function chooseBestSum($t, $k, $ls) {
				
				echo "t:"; print_r($t); echo "<br>";
				echo "k:"; print_r($k); echo "<br>";
				echo "list:"; print_r($ls); echo "<br>";
				
				$lenght = count($ls);
				if($k>count($ls)){
					return null;
				}
				if($t<3){
					return null;
				}
				$list = $ls;
				sort($list);
				print_r($list);
				$su=0;
				for($i=0; $i<$k; $i++){
					$su += $list[$i];
				}
				if($su > $t){
					return null;
				}
				/*
				for($i=$length; $i>$k; $i--){
					$ksum = $list[$i];
					for($j=0; $j<$k-1; $j++){
						$ksum += $list[$j];
					}
					if($ksum>$t && $list[$i] != $t+1){
						$element = array_search($ls, $list[i]);
						while($element != false){
							$ls[$element] = $t + 1;
							$element = array_search($ls, $list[i]);
						}
						
					}
				}*/
				$lenght = count($list);
				//$i = $lenght;
				$max_sum = find_sum($k-1,0,$ls,$t,0, $k-1);
				
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
				echo "<br>";
				echo "<br>";
				return $max_sum;
			}
			
			
			
			
			
			
			
			$ts = [50, 55, 56, 57, 58];
			echo chooseBestSum(163, 3, $ts);
			
			//$ts = [91, 74, 73, 85, 73, 81, 87];
			//echo chooseBestSum(230, 3, $ts);
			
			//$ts = [91, 74, 73, 85, 73, 81, 87];
			//echo chooseBestSum(331, 5, $ts);
			//$ts = [50];
			//echo chooseBestSum(163, 3, $ts);
			
			//$ts = [1000, 640, 1230, 2333, 1440, 500, 1320, 1230, 340, 890, 732, 1346];
			//echo chooseBestSum(2300, 4, $ts);
			
			function test(){
				return [[1,2],3];
			}
			
			$t = test()[0][1];
			//echo $t;
			

		?>
		
		
		<form action="site.php" method="post">
			
			<input type="submit">
		</form>

		
		
	</body>


</html>
