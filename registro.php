<?php
    $client = new MongoDB\Client(
        'mongodb+srv://<username>:luisgarcia15@<cluster-address>/test?retryWrites=true&w=majority'
    );
    $db = $client->registros;
    $visita = $db->selectCollection($db,"registro_visitas");

    $nombre = $_POST["nombre"];
    $correo = $_POST["correo"];
    $edad = $_POST["edad"];

    $nuevavisita->insertOne(array("nombre" => $nombre, "correo" => $correo, "edad" => $edad));
?>
