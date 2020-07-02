<?php 
    if(isset($_POST['title'])){
        setcookie('title',$_POST['title'],time()+(60*60*24*7));
?>
    <p>Titular definido correctamente</p>
<?php
    }
?>
<a href="http://localhost/Codigos/Practica%207/Ejercicio%204/">Volver a la página princial</a>