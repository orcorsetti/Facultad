<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practica 7 - Ejercicio 1</title>
</head>
<body>
    <?php 
        require('./scripts.php')
    ?>
    <form action="scripts.php" method="post">
        <p>Seleccione el estilo que desee:</p>
        <select name="style" id="style">
            <option value="gray">Gris</option>
            <option value="green">Verde</option>
            <option value="red">Rojo</option>
        </select>
        <input type="submit" value="Actualizar Estilo de Página">
    </form>
</body>
</html>