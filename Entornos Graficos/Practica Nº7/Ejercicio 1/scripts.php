<?php
    if(isset($_POST['style'])){
        $style = $_POST['style'];
        setcookie('style', $style, time()+(60*60*24*365));
?>
<p>Tema definido correctamente!</p>
<a href="http://localhost/Codigos/Practica%207/Ejercicio%201/">Volver Atrás</a>
<?php
    } else {
        if(isset($_COOKIE['style'])){
            $style=$_COOKIE['style'];
        }
    }
    if(isset($style)){
        echo '<link rel="stylesheet" href="./styles/'.$style.'.css">';
    }
?>
<link rel="stylesheet" href="./styles/'.$style.'.css">