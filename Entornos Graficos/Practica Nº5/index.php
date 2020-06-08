<?php
    session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practica 5</title>
</head>
<body>
    <?php 
        require './counter.php';
    ?>
    <h1>Practica 5</h1>
    <a href="./Ejercicio 1/index.php">Ejercicio 1</a>
    <a href="./Ejercicio 2/index.php">Ejercicio 2</a>
    <a href="./Ejercicio 3/index.php">Ejercicio 3</a>

    <p>
    <?php
        echo "Has visitado ".$_SESSION['contador']." páginas";
    ?></p>
</body>
</html>