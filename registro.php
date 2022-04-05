<?php
    $serverApi = new ServerApi(ServerApi::V1);
    $client = new MongoDB\Client(
        'mongodb+srv://luisgarcia:luisgarcia15@cluster0.7nfcf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', [], ['serverApi' => $serverApi]);
    $db = $client->test;
    $collection = $db->users;

    $nombre = $_POST['nombre'];
    $correo = $_POST['email'];
    $edad = $_POST['edad'];

    $document = [
        'nombre' => $nombre,
        'correo' => $correo,
        'edad' => $edad
    ];

    $collection->insertOne($document);
?>
