<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practica 7 - Ejercicio 2</title>
</head>
<body>
    <?php
        if(isset($_COOKIE['counter'])){
            echo '<p>Bienvenido de nuevo!</p>';
            echo '<p>Cantidad de visitas: '.$_COOKIE['counter'].'</p>';
            setcookie('counter',$_COOKIE['counter']+1,time()+(60*60*24*365));
        } else {
            echo '<p>Bienvenido al sitio!</p>';
            echo '<p>Cantidad de visitas: Primera visita!</p>';
            setcookie('counter',1,time()+(60*60*24*365));
        }
    ?>
</body>
</html>