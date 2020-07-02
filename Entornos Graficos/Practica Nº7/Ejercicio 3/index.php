<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practica 7 - Ejercicio 3</title>
</head>
<body>
    <?php
    if(isset($_POST['username'])){
        setcookie('username', $_POST['username'], time()+(60*60*24*365));
        echo "<meta http-equiv='refresh' content='0'>";
    }
    if(isset($_COOKIE['username'])){
    ?>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <p>Ingese su nombre de usuario</p>
        <input type="text" name="username" id="username" value="<?php echo $_COOKIE['username']?>" required>
        <input type="submit" value="Actualizar">
    </form>
    <?php
    } else {
    ?>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <p>Ingese su nombre de usuario</p>
        <input type="text" name="username" id="username"  required>
        <input type="submit" value="Actualizar">
    </form>
    <?php
    }
    ?>
</body>
</html>