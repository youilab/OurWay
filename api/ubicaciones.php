<?php

$id_ruta = $_GET["id"];

$enlace = mysqli_connect("127.0.0.1", "root", "mrHDEZ93.", "OurWay");

$ubicaciones = array();

if ($resultado = $enlace->query("select LATITUDE, LONGITUDE, TIMESTAMP from Ubicaciones where ID_RUTA = " . $id_ruta . " ORDER BY ID DESC LIMIT 1;")){

	while ($fila = $resultado->fetch_row()) {
		$tmp = new stdClass();
		$tmp->{"lat"} = $fila[0];
		$tmp->{"lng"} = $fila[1];
		$tmp->{"timestamp"} = $fila[2];
		array_push($ubicaciones, $tmp);
    }
}

echo json_encode($ubicaciones);

?>