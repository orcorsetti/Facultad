<?php 
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practica 7 - Ejercicio 5</title>
</head>
<body>
    <form action="createSession.php" method="post">
        <input type="text" name="username" id="username" required>
        <input type="password" name="password" id="password" required>
        <input type="submit" value="Guardar" name="session">
    </form>
    <form action="recoverSession.php" method="get">
        <input type="submit" value="Recuperar Variables">
    </form>
</body>
</html>
