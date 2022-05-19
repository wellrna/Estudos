<!DOCTYPE html>
<html>

	<head>
		<meta charset="utf-8">
		<title>Meu Primeiro Site Pessoal WELL!!! Woohoo"</title>
		<link rel="stylesheet" href="/HTML-CSS/EX1/style.css">
	</head>
	
	<body>

		<header>
		
			<img src="/HTML-CSS/EX1/image1.jpg" alt="imagem decorativa" class="photo"></img>
			<h1 id="title">Wellington Nunes</h1><br /><br />
		</header>

		<section>

			<header>
				<h2 class="subtitle">Novidades</h2>
			</header>

			<article class="post">

				<header>
					<h3 class="post_title">POST #1</h3>
				</header>

				<o class="post_content">
					<img src="/HTML-CSS/EX1/abelha.png" alt="foto abelha jataí" class="post_image"></img><br />
					ZUM-ZUM E MEL<br />
					Como abelhas nativas mudaram a vida e o entorno da casa de um artista em Santa Teresa, no Rio de Janeiro<br />
					Veja mais em <a href="https://www.uol.com.br/ecoa/reportagens-especiais/abelhas-sem-ferrao-mudaram-a-vida-de-um-artista-no-rio/#cover" target="_blank">ECOA UOL</a> <br /><br />
				</o>

				<header>
					<h3 class="post_title">POST #2</h3>
				</header>

				<o>
					<img src="https://conteudo.imguol.com.br/c/entretenimento/cb/2022/04/13/as-oncas-maiara-e-maraisa-que-estao-no-parque-ambiental-chico-mendes-em-rio-branco-ac-1649882158729_v2_450x450.jpg" alt="foto dos filhotes de onça pintada"></img><br />
					Onças-pintadas Maiara e Maraísa fazem visitas a parque dobrar: "sucesso"...<br />
					Veja mais em <a href="https://www.uol.com.br/ecoa/ultimas-noticias/2022/04/14/oncas-pintadas-maiara-e-maraisa-fazem-visitas-em-parque-dobrar-sucesso.htm" target="_blank">ECOA UOL</a> <br /><br />
				</o>

				<img src="/HTML-CSS/EX1/i1.jpg" alt="Exemplo de imagem que não abriu" class="photo2"></img><br /><br />				

				<?php
				print( "CONTEÚDO PHP<br /><br />");
				for ( $i = 0; $i < 10; $i++ ) {
					print( "Linha número " . $i . "<br />");
					}
				?><br /><br />

				<script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
				<script type="text/javascript">
					$(document).ready(function() { 
						console.log("CONTEÚDO JAVASCRIPT - Woohoo!!!");
						alert("CONTEÚDO JAVASCRIPT - Woohoo!!!");
						//c:/Users/XXX/Pictures/Well.png
					});
				</script>
			
			</article>
		</section>

		<footer>

			<img src="/HTML-CSS/EX1/image1.jpg" alt="foto do rosto de Wellington" class="photo2"></img><br /><br />

			<ul>
				<li>
			<a>LINK</a>
				</li>
				<li>
					Contatos: <a href="tel:0911999911999" class="a1">Celular/Whatsapp: +55 911 99991-1999 </a>
				</li>
				<Li>
					<a href="mailto:well.rna@gmail.com" class="a1">E-mail: well.rna@gmail.com</a><br />
				</li>
				<li>
					<a href="https://www.linkedin.com/in/wellrna" target="_blank" class="a2">Linkedin</a>
				</li>
				<li>
					<a href="https://github.com/wellrna/dio-desafio-github.git" target="_blank" class="a3">GITHUB-Desafio_DIO</a>
				</li>
				<li>
					<a target="_blank" class="a4">Link - faz o link abrir em nova aba // ul - lista não ordenada <br />
						ol - lista ordenada // li - itens da lista // </a>
				</li>
			</ul>
		</footer>
	</body>
	
</html>

