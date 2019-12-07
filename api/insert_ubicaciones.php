<?php

$id_ruta = $_POST["id"];
$lat = $_POST["lat"];
$lng = $_POST["lng"];
$timestamp = $_POST["timestamp"];

$enlace = mysqli_connect("127.0.0.1", "root", "mrHDEZ93.", "OurWay");

$ubicaciones = array();

$query = "INSERT INTO Ubicaciones (ID_RUTA, LATITUDE, LONGITUDE, TIMESTAMP) VALUES (" . $id_ruta . ", " . $lat . ", " . $lng . ", " . $timestamp . ")";
$enlace->query($query);

$enlace->close();

echo "DONE";

?>