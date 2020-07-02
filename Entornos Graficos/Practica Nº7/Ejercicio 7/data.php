<?php
    $hostname = 'localhost';
    $username = 'orcorsetti';
    $pass = '';
    $db = 'compras';

    $conn = new mysqli($hostname,$username,$pass);
    if($conn->connect_error){
        echo'<script type="text/javascript">
            alert("Error: '.$conn->connect_error.'");
            window.location.href="index.php";
        </script>';
    }
    mysqli_select_db($conn,$db);

    $sql = 'SELECT * FROM catalogo';
    $result = $conn->query($sql) or die($conn->error);
    if(mysqli_num_rows($result)==0){
        $products = false;
    } else{
        $products= true;
    }
?>