<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title></title>
	</head>
	<body>		

		
		<?php
			function greet($name) {
				$phrase = strtolower($name);
				$phrase[0] = strtoupper($phrase[0]);
				echo "Hello $phrase!";
  
			}
			function greet1($name) {
				return "Hello " . mb_convert_case($name, MB_CASE_TITLE) . "!";
			}
			function greet2($name) {
			  return sprintf("Hello %s!", ucwords(strtolower($name)));
			}
			
			greet("JOHN");
			
			function DNA_strand($dna) {
				$second_dna = "";
				for($i=0; $i<strlen($dna); $i++){
					switch($dna[$i]){
						case "A":
							$second_dna[$i] = "T";
							break;
						case "T":
							$second_dna[$i] = "A";
							break;
						case "C":
							$second_dna[$i] = "G";
							break;
						case "G":
							$second_dna[$i] = "C";
							break;
					}
				}
				return $second_dna;
				
			}
			$second_dna = DNA_strand("AATTCCGG");
			for ($j=0; $j<strlen($second_dna);$j++){
				echo $second_dna[$j];
			}
			
			function DNA_strand1($dna) {
			  return strtr($dna, ['A'=>'T', 'T'=>'A', 'C'=>'G', 'G'=>'C']);
			}
			
			function DNA_strand2($dna) {

			  $conversion = ["A"=>"T","T"=>"A","G"=>"C", "C"=>"G"] ; 
			  $dna = str_split($dna) ;
			  $res = "" ; 
			  foreach($dna as $el){
				$res .= $conversion[$el] ;  
			  }
			  return $res ; 
			   
			   
			}
			
			function stray($arr){
				$prev = $arr[0];
				for($i=1; $i<count($arr)-1; $i++){
					if($arr[$i]!=$prev){
						if($arr[$i]!=$arr[$i+1]){
							return $arr[$i];
						}elseif($prev != $arr[$i+1]){
							return $prev;
							
						}
					}
					
				}
				return end($arr);
			}
			echo stray([4, 4, 4, 5, 4, 4, 4]);
			echo stray([4, 2, 2, 2, 2]);
			
			function stray1(array $arr) {
			  return array_search(1, array_count_values($arr));
			}
			
			function stray2($arr){
			  sort($arr);
			  return $arr['0'] ==  $arr['1'] ? end($arr) : $arr['0'];
			}
			
			function encode2(string $s): string {
				$arr = [];
				$j=0;
				$number = 1;
				foreach(range("a", "z") as $i){
					echo "$i";
					$arr += [$i => $number];
					$number = abs($number - 1);
					print $arr[$i];
					echo "<br>";
				}
				$arr += [" " => " "];
				$chars = str_split($s);
				$str = "";
				foreach($chars as $char){
					$str = $str . $arr[$char];
					//print($char);
					//echo "<br>";
				}
				return $str;
			}
			
			function encode3(string $s): string {
				$arr = [];
				$j=0;
				//$number = 1;

				foreach(range("a", "z") as $i){
					array_push($arr, $i);
					//$number = abs($number - 1);
				}
				//$arr += [" " => " "];
				$chars = str_split($s);
				$str = "";
				$i=0;
				foreach($chars as $char){
					//if(in_array($char, range("a", "z")){
					//	$str = $str . $arr[$char];
					//}
					if(in_array($char, $arr)){
						$str = $str . array_search($char, $arr)%2;
					}else{
						$str = $str . $char;
					}

					
				}
				return $str;
			}
			
			function encode4(string $s): string {
			  return preg_replace_callback('/[a-z]/i', function ($m) {return (ord($m[0]) + 1) % 2;}, $s);
			}
			
			function encode5(string $s): string {
			  return implode(array_map(function ($e) {
				  return ctype_alpha($e) ? (ord($e) + 1) % 2 : $e;
				}, str_split($s)));
			}
			
			//echo encode("sdf d fsfsd");
			
			$greet = function($name) {
				printf("Hello %s\r\n", $name);
			};
			$greet("PHP");
			
			echo preg_replace_callback('~-([a-z])~', function ($match) {
				return strtoupper($match[1]);
			}, 'hello-world');
			echo "<br>";
			echo "<br>";
			
			
			function camel_case(string $s): string {
				$s = trim($s);
				$words = explode(" ", $s);
				$result = "";
				foreach($words as $word){
					$word[0] = strtoupper($word[0]);
					$result = $result . $word;
				}
				//print_r($arr);
				return $result;
			  // Your code here
			}
			echo camel_case("Hello case");
			echo camel_case(" camel case word");
			echo camel_case("test case");
			
			function camel_case1(string $s): string {
			  return str_replace(' ', '', ucwords(trim($s)));
			}
			
			function camel_case2(string $s): string {
				return empty($s) ? "" : implode(array_map('ucfirst', explode(" ", trim($s))));
			}
			echo "<br>";
			
			function digPow($n, $p) {
				$original = $n;
				$sum = 0;
				$p += strlen(strval($n));
				while($n>=1){
					$p--;
					$no = $n % 10;
					$sum += pow($no, $p);
					$n = floor($n/10);
				}

				$product = $original;
				$count = 1;
				while($product <= $sum){
					if($product == $sum){
						return $count;
					}
					$product += $original;
					$count++;
					
				}
				return -1;
			}
			
			//echo digPow(153,1);
			//echo digPow(92, 1);
			//echo digPow(89, 1);
			echo digPow(46288, 3);
			
			function digPow2($n, $p) {
				$sum = 0;
				
				foreach(str_split($n) as $number) {
					$sum += $number ** $p++;
				}
				  
				return (($sum % $n) == 0) ? 
					($sum / $n) : -1 ;
			}
			
			function digPow3($n, $p) {
				// Split $n into array
				$digits = str_split($n);
			   
				// Walk through digits to calculate x ^ p + index
				array_walk($digits, function (&$elem, $index, $param) { $elem = pow($elem, $param + $index); }, $p);
				
				// Calculate sum
				$calc_result = array_sum($digits);
				
				// Return $calc_result / $n if $calc_result % $n == 0, return -1 otherwise
				return (($calc_result % $n == 0) ? ($calc_result / $n) : -1);
			}
			
			function find($integers) {
				$divider = 0;
				if($integers[0]%2 ==$integers[1]%2){
					$divider = $integers[0]%2;
				}else{
					if($integers[0]%2 == $integers[2]%2){
						return $integers[1];
					}else{
						return $integers[0];
					}
				}
				
				for($i=2; $i<count($integers);$i++){
					if(abs($integers[$i]%2) != $divider){
						return $integers[$i];
					}
				}
				
			}
			
			$go = 0;
			
			function calculation1($catch_up_rate){
				global $go;
				$result = 0;
				if($catch_up_rate==0){
					return 0;
				}
				$co = 0;
				while($go - $catch_up_rate>=0 && $co<100){
					$go = $go - $catch_up_rate;
					$result++;
					$co++;
				}
				return $result;
			
			}
			
			function race1($v1, $v2, $g) {
				global $go;
				$go = $g;
				$catch_up_rate = $v2 - $v1;
				$hour = calculation1($catch_up_rate);	
				//$minutes = calculation1(ceil($catch_up_rate/60));
				//$seconds = calculation1(ceil($catch_up_rate/3600));
				$go *= 60;
				$minutes = calculation1($catch_up_rate);
				$go *= 60;
				$seconds = calculation1($catch_up_rate);
				$arr = array($hour,$minutes,$seconds);
				print_r($arr);
			}
			
			//print_r(race(720, 850, 70));
			//print_r(race(80, 91, 37));
			//print_r(race(80, 100, 40));
			print_r(race1(541, 621, 144));
			
			function race2($v1, $v2, $g) {
			  if($v1 >= $v2) return null;
			  $h = $g / ($v2 - $v1);
			  return [floor($h), (floor($h * 60) % 60), floor($h * 3600) % 60];
			}
			
			
			
		?>
		
		
		<form action="site.php" method="post">
			
			<input type="submit">
		</form>

		
		
	</body>


</html>