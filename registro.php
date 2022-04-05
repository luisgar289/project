<?php
    $client = new MongoDB\Client('mongodb+srv://luisgarcia:luisgarcia15@cluster0.7nfcf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority');
    $db = $cliente->selectDB("registros");
    $visita = $db->selectCollection($db,"registro_visitas");

    $nombre = $_POST["nombre"];
    $correo = $_POST["correo"];
    $edad = $_POST["edad"];

    $nuevavisita->insertOne(array("nombre" => $nombre, "correo" => $correo, "edad" => $edad));
?>
