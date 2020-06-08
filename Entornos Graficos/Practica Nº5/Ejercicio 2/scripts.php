<?php
    if(isset($_POST['sendComment'])) {
        $name = $_POST['name'];
        $from = $_POST['email'];
        $msg = $_POST['comment'];
        $subject = "Consulta desde la Web de ${name}";

        $headers = 'From: '.$from."\r\n".
        'Reply-To: '.$from."\r\n" .
        'X-Mailer: PHP/' . phpversion();

        $to = "orcorsetti@gmail.com";

        if(mail($to, $subject, $msg, $headers)) {
            echo 'Envio realizado correctamente.';
        } else {
            echo 'Error en el envío.';
        }
    }
?>