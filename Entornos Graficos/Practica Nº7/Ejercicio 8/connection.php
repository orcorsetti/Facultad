<?php
    $hostname = 'localhost';
    $username = 'orcorsetti';
    $pass = '';
    $db = 'prueba';

    $conn = new mysqli($hostname,$username,$pass);
    if($conn->connect_error){
        echo'<script type="text/javascript">
            alert("Error: '.$conn->connect_error.'");
            window.location.href="index.php";
        </script>';
    }
    mysqli_select_db($conn,$db);
?>