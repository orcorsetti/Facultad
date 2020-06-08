<?php
    if(isset($_POST['sharePage'])){
        $to = $_POST['emailTo'];
        $subject = 'Hecha un vistazo a esta página';
        $msg = 'Te recomiendo que veas la siguiente página: https://entornosgraficos-practica5.000webhostapp.com/Ejercicio%202/scripts.php';
        $from = $_POST['emailFrom'];

        $headers = 'From: '.$from."\r\n".
        'Reply-To: '.$from."\r\n" .
        'X-Mailer: PHP/' . phpversion();
        
        if(mail($to, $subject, $msg, $headers)){
            echo 'Envio realizado correctamente';
        } else {
            echo 'Error en el envío';
        }
    }
?>