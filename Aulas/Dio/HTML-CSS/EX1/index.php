<html>

	<head>
		<title>Meu primeiro site em PHP! Woohoo"</title>

		<script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>

		<style type="text/css">
			.linha {
				font-weight: bold;
				color: green;
				padding-left: 10px;
				line-height: 50px;
			}
		</style>
	</head>
	
	<body>
	
		<?php
			for ( $i = 0; $i < 11; $i++ ) {
				print( "Linha número " . $i . "<br />");
			}
		?>
		
	</body>
	
	<script type="text/javascript">
		$(document).ready(function() {
			alert("Woohoo!!!");
		});
	</script>
	
</html>

