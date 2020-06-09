<?php
    $hostname = 'localhost';
    $user = 'orcorsetti';
    $pass = 'orcorsetti';
    $db = 'capitales';

    function getData(){
        $conn = mysqli_connect($GLOBALS['hostname'],$GLOBALS['user'],$GLOBALS['pass']);

        if(mysqli_select_db($conn,$GLOBALS['db'])){
            $query = 'SELECT * FROM ciudades';
            $result = $conn -> query($query) or die($conn->error);
            $conn->close();
            return $result;
        } else {
            throw new Exception('Error al conectar con la Base de Datos.');
        }
    } 
?>