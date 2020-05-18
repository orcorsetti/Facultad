<!-- Página que verifica el usuario -->
<html>
<head></head>
<body>
<?php
    include './control.php';
    if (!isset($_POST['submit'])) {
    ?>
<form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post">
    Usuario: <input type="text" name="user">
    <input type="submit" name="submit" value="Registrar">
</form>
<?php
    }
    else {
        $usuario = $_POST['user'];
        comprobar_nombre_usuario($usuario); 
    }
?>
</body>
