<?php
    session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practica 5 - Ejercicio 2</title>
</head>
<body>
    <?php
        require '../counter.php';
    ?>
    <form action="scripts.php" method="post">
        <p>Nombre: <input type="text" name="name" id="name" placeholder="Inserte su Nombre aqui" required></p>
        <p>Email: <input type="email" name="email" id="email" placeholder="Inserte su Email aqui" required></p>
        <p>Consulta: <textarea name="comment" id="comment" cols="30" rows="10" placeholder="Ingrese su consulta aqui" required></textarea></p>
        <button type="submit" name="sendComment">Enviar</button>
    </form>
    <br>
    <p>
    <?php
        echo "Has visitado ".$_SESSION['contador']." páginas";
    ?></p>
</body>
</html>