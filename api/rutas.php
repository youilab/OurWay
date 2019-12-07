<?php

$enlace = mysqli_connect("127.0.0.1", "root", "mrHDEZ93.", "OurWay");

$rutas = array();

if ($resultado = $enlace->query("select * from Rutas;")){

	while ($fila = $resultado->fetch_row()) {
		$tmp = new stdClass();
		$tmp->{"id"} = $fila[0];
		$tmp->{"url"} = $fila[1];
		$tmp->{"nombre"} = $fila[2];
		array_push($rutas, $tmp);
    }
}

echo json_encode($rutas);

?>