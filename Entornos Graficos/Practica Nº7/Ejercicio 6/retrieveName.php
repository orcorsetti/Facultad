<?php
    session_start();
    if(isset($_SESSION['name'])){
?>
<p>Nombre del Alumno: <?php echo $_SESSION['name']?></p>
<?php
    } else {
        echo "<p>No tiene permiso para acceder a esta página</p>";
    }
?>
<a href="http://localhost/Codigos/Practica%207/Ejercicio%206/">Volver a la pagina principal</a>