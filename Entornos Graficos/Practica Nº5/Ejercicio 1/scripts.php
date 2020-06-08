<?php 

    $to = "orcorsetti@gmail.com";
    $subject = "Holis";
    $from = "orcorsetti@gmail.com";

    $headers  = 'MIME-Version: 1.0' . "\r\n";
    $headers .= 'Content-type: text/html; charset=iso-8859-1' . "\r\n";

    $headers .= 'From: '.$from."\r\n".
    'Reply-To: '.$from."\r\n" .
    'X-Mailer: PHP/' . phpversion();

    $message = '<html><body>';
    $message .= '<h1>Practica Numero 5 PHP</h1>';
    $message .= '<p style="color:#080;font-size:18px;">Prueba Ejercicio 1</p>';
    $message .= '</body></html>';

    if(mail($to,$subject,$message,$headers)){
        echo 'El mail se envio correctamente.';
    } else {
        echo 'Imposible enviar el mail.';
    }

?>