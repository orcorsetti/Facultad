<?php
    session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicio 3</title>
</head>
<body>
    <?php
        require '../counter.php';
    ?>
    <p>Desea compartir el sitio?</p>
    <form action="scripts.php" method="post">
        <p>Tu Email: <input required type="email" name="emailFrom" id="emailFrom" placeholder="Inserte su email aqui"></p>
        <p>Email de amigo: <input required type="email" name="emailTo" id="emailTo" placeholder="Inserte el email de su amigo aqui"></p>
        <button type="submit" name="sharePage">Enviar</button>
    </form>
    <br>
    <p>
    <?php
        echo "Has visitado ".$_SESSION['contador']." páginas";
    ?></p>
</body>
</html>