<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
    <link rel="icon" type="image/png" href="../favicon.ico">
    <link rel="apple-touch-icon" sizes="76x76" href="../favicon.ico">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

    <title>SPARKfly | Terms of Service</title>

    <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport' />
    <meta name="viewport" content="width=device-width" />

    <link href="../assets/css/bootstrap.min.css" rel="stylesheet" />
    <link href="../assets/css/paper-kit.css?v=2.1.0" rel="stylesheet"/>
    <link href="../assets/css/demo.css" rel="stylesheet" />

    <!--     Fonts and icons     -->
    <link href='https://fonts.googleapis.com/css?family=Montserrat:400,300,700' rel='stylesheet' type='text/css'>
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css" rel="stylesheet">
    <link href="../assets/css/nucleo-icons.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap" rel="stylesheet">
	<script src="https://kit.fontawesome.com/2c36e9b7b1.js"></script>
	<link rel="stylesheet" href="estilos.css">


</head>

<body class="blog-page">

<?php $whitepage = 1; include '../assets/include/menu.php'; ?>

    <div class="wrapper">
        <div class="main">
          <div class="contenedor">
		<header>
			<div class="logo">
				<br>
				<h1>Image Portfolio</h1>
			
			</div>
			<form action="">
				<input type="text" class="barra-busqueda" id="barra-busqueda" placeholder="Buscar">
			</form>
			<div class="categorias" id="categorias">
				<a href="#" class="activo">Todos</a>
				<a href="#">Restaurant</a><!-- naturaleza Pluginh/ -->
				<a href="#">Store</a><!--  Pluginh/ -->
				<a href="#">Home</a><!--  Pluginh/ -->
				<a href="#">Couples</a><!--  Pluginh/ -->
				<a href="#">Music</a><!--  Pluginh/ -->
				<a href="#">Games</a><!--  Pluginh/ -->
				<a href="#">Pets</a><!--  Pluginh/ -->
				<a href="#">scenery</a><!--  Pluginh/ -->
			</div>
		</header>

		<section class="grid" id="grid">
			<div class="item" 
				 data-categoria="restaurant"
				 data-etiquetas="restaurant "
				 data-descripcion="Preparing a meal as a couple"
			>
				<div class="item-contenido">
					<img src="img/comida1.jpg" style="width: 200px; height: 250px;" alt="">
				</div>
			</div>
			<div class="item" 
				 data-categoria="restaurant"
				 data-etiquetas="restaurant"
				 data-descripcion="buying food utensil"
			>
				<div class="item-contenido">
					<img src="img/comida2.jpg" style="width: 200px; height: 250px;" alt="">
				</div>
			</div>
			<div class="item" 
				 data-categoria="couples"
				 data-etiquetas="couples"
				 data-descripcion="buying food utensil"
			>
				<div class="item-contenido">
					<img src="img/pareja.png" style="width: 200px; height: 250px;" alt="">
				</div>
			</div>
			<div class="item" 
				 data-categoria="couples"
				 data-etiquetas="couples"
				 data-descripcion="buying food utensil"
			>
				<div class="item-contenido">
					<img src="img/pareja1.jpg" style="width: 200px; height: 250px;" alt="">
				</div>
			</div>
			<div class="item" 
				 data-categoria="couples"
				 data-etiquetas="couples"
				 data-descripcion="buying food utensil"
			>
				<div class="item-contenido">
					<img src="img/pareja3.jpeg" style="width: 200px; height: 250px;" alt="">
				</div>
			</div>
			<div class="item" 
				 data-categoria="scenery"
				 data-etiquetas="scenery"
				 data-descripcion="buying food utensil"
			>
				<div class="item-contenido">
					<img src="img/paisaje.jpg" style="width: 200px; height: 250px;" alt="">
				</div>
			</div>

<div class="item" 
				 data-categoria="scenery"
				 data-etiquetas="scenery"
				 data-descripcion="buying food utensil"
			>
				<div class="item-contenido">
					<img src="img/paisaje.png" style="width: 200px; height: 250px;" alt="">
				</div>
			</div>



			
		</section>

		<section class="overlay" id="overlay">
			<div class="contenedor-img">
				<button id="btn-cerrar-popup"><i class="fas fa-times"></i></button>
				<img src="" alt="">
			</div>
			<p class="descripcion"></p>
		</section>

		<footer class="contenedor">
			<div class="redes-sociales">
				<div class="contenedor-icono">
					<a href="#" target="_blank" class="twitter">
						<i class="fab fa-twitter"></i>
					</a>
				</div>
				<div class="contenedor-icono">
					<a href="#" target="_blank" class="facebook">
						<i class="fab fa-facebook-f"></i>
					</a>
				</div>
				<div class="contenedor-icono">
					<a href="#" target="_blank" class="instagram">
						<i class="fab fa-instagram"></i>
					</a>
				</div>
			</div>
			
		</footer>
	</div>

	<script src="https://unpkg.com/web-animations-js@2.3.2/web-animations.min.js"></script>
	<script src="https://unpkg.com/muuri@0.8.0/dist/muuri.min.js"></script>
	<script src="main.js"></script>
	


                            </div>

<?php include '../assets/include/footer.php'; ?>
</body>


<!-- Core JS Files -->
<script src="../assets/js/jquery-3.2.1.min.js" type="text/javascript"></script>
<script src="../assets/js/jquery-ui-1.12.1.custom.min.js" type="text/javascript"></script>
<script src="../assets/js/popper.js" type="text/javascript"></script>
<script src="../assets/js/bootstrap.min.js" type="text/javascript"></script>

<!-- Control Center for Paper Kit: parallax effects, scripts for the example pages etc -->
<script src="../assets/js/paper-kit.js?v=2.1.0"></script>

</html>




