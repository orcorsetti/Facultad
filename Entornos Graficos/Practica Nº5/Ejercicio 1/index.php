<?php
    session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practica 5 - Ejercicio 1</title>
</head>
<body>
    <?php
        require '../counter.php';
    ?>
    <h1>Entornos Graficos - Practica 5</h1>
    <br>
    <p>Ejercicio 1</p>
    <form action="scripts.php" method="post">
        <button type="submit" name="send_message">Enviar Mensaje</button>
    </form> 
    <br>
    <p>
    <?php
        echo "Has visitado ".$_SESSION['contador']." páginas";
    ?></p>
</body>
</html>