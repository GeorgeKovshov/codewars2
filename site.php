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
			
		?>
		
		
		<form action="site.php" method="post">
			
			<input type="submit">
		</form>

		
		
	</body>


</html>
