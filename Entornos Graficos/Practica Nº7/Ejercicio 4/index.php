<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practica 7 - Ejercicio 4</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Diario</h1>
    <?php
        error_reporting(E_ALL ^ E_NOTICE); 
        if(!(isset($_COOKIE['title']))){
    ?>
        <form action="defineCookie.php" method="post">
            <p><input type="radio" name="title" id="title" value="sports">Noticia Deportiva</p>
            <p><input type="radio" name="title" id="title" value="economics">Noticia Económica</p>
            <p><input type="radio" name="title" id="title" value="politics">Noticia Política</p>
            <input type="submit" value="Definir Titular">
        </form>
    <?php
        } else {
    ?>
        <form action="deleteCookie.php" method="post">
            <input type="submit" value="Eliminar Titular">   
        </form>
    <?php
        }
        if($_COOKIE['title']=='sports' or !(isset($_COOKIE['title']))){
    ?>
        <div class="news">
            <h2>Titulo Noticia Deportiva</h2>
            <h3>Subtitulo Noticia Deportiva</h3>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Expedita aspernatur ratione ipsum suscipit ad id vel non sunt, error eius, ullam praesentium, enim iste? Possimus soluta reprehenderit nesciunt! Accusantium, enim.</p>
        </div>
    <?php
        } 
        if($_COOKIE['title']=='economics' or !(isset($_COOKIE['title']))){
    ?>
        <div class="news">
            <h2>Titulo Noticia Económica</h2>
            <h3>Subtitulo Noticia Económica</h3>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Expedita aspernatur ratione ipsum suscipit ad id vel non sunt, error eius, ullam praesentium, enim iste? Possimus soluta reprehenderit nesciunt! Accusantium, enim.</p>
        </div>
    <?php
        } 
        if($_COOKIE['title']=='politics' or !(isset($_COOKIE['title']))) {
    ?>
        <div class="news">
            <h2>Titulo Noticia Política</h2>
            <h3>Subtitulo Noticia Política</h3>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Expedita aspernatur ratione ipsum suscipit ad id vel non sunt, error eius, ullam praesentium, enim iste? Possimus soluta reprehenderit nesciunt! Accusantium, enim.</p>
        </div>
    <?php        
        }
         
    ?>
</body>
</html>