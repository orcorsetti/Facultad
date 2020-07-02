<?php
    session_start();
    if(isset($_POST['create'])){   
        $servername = 'localhost';
        $username = 'orcorsetti';
        $pass = '';
        $dbname = 'base2';

        $conn = new mysqli($servername,$username, $pass);

        if($conn->connect_error){
            die('Error de conexión: '.$conn->connect_error);
        }
        
        mysqli_select_db($conn,$dbname);

        $sql = 'SELECT `nombre` FROM `alumnos` WHERE `mail`="'.$_POST['mail'].'"';
        $result = $conn->query($sql) or die($conn->error);
        if(mysqli_num_rows($result)!=0){
            $row = $result->fetch_row();
            $_SESSION['name'] = $row[0];
?>
        <p>Nombre recuperado correctamente.</p>
<?php
        } else {    
            unset($_SESSION['name']);
?>
        <p>Email incorrecto.</p>
<?php
        }
        $conn->close();
    }
?>
<a href="http://localhost/Codigos/Practica%207/Ejercicio%206/">Volver a la pagina principal</a>