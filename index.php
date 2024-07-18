<!DOCTYPE html>
<html>
<head>
	<title>Formulario</title>
	<style>
		form {
			border-style: solid;
			border-width: 5px;
			width: 400px;
			color: lightgreen;
		}
	
	</style>
</head>
<body>
<div style="margin-left:400px">
	<form action="procesar.php" method= "post">

		Nombre: <input type="text" name="nombre">
		
		<br>
		Correo Electronico: <input type="text" name="correo">
		
		<br>
		Direccion: <input type="text" name="direccion">
	<input type  = "submit" value = "Enviar">

	</form>

	
	

</div>
</body>
</html>