<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>    
    <?php 
        $hostname = 'localhost';
        $user = 'orcorsetti';
        $pass = 'orcorsetti';
        $db = 'capitales';
        if(isset($_POST['editButton'])){
            if(isset($_POST['radio_group'])){
                $editDisplay='block';
                $conn = mysqli_connect($GLOBALS['hostname'],$GLOBALS['user'],$GLOBALS['pass']);
                mysqli_select_db($conn, $db);
                $id = $_POST['radio_group'];

                $query = "SELECT * FROM ciudades WHERE id =".$id."";
                $result = $conn-> query($query) or die($conn->error);
                $conn ->close();
                $row = $result->fetch_assoc();
                $metro='';
                if($row['tieneMetro']==1){
                    $metro = 'checked';
                } 
                echo "<div class='editForm'>
                        <h1>Editar</h1>
                        <form action='query.php' method='post'>
                            <p>ID: <input type='text' name='id' readonly value='".$row['id']."'></p>
                            <p>Ciudad: <input required type='text' name='ciudad' value='".$row['ciudad']."'></p>
                            <p>País: <input required type='text' name='pais' value='".$row['pais']."'></p>
                            <p>Habitantes: <input required type='number' name='habitantes' value='".$row['habitantes']."'></p>
                            <p>Superficie: <input required type='number' name='superficie' value='".$row['superficie']."'></p>
                            <input type='hidden' name='tieneMetro' value='0'>
                            <p>Tiene Metro: <input type='checkbox' name='tieneMetro' value='1' ".$metro." ></p>
                            <a href='./index.php' class='secondaryButton' >Cancelar</a>
                            <button type='submit' class='primaryButton' name='editRow'>Aceptar</button>
                        </form>
                    </div>";
            } else {
                echo
                    "<div class='msg'>". 
                    "<p>Debe seleccionar un elemento</p>".
                    "<a href='./index.php' class='primaryButton'>Volver</a>".
                    "</div>";
            }
            
        }

        if(isset($_POST['editRow'])){
            $conn = mysqli_connect($GLOBALS['hostname'],$GLOBALS['user'],$GLOBALS['pass']);
            
            $id = $_POST['id'];
            $ciudad = $_POST['ciudad'];
            $pais = $_POST['pais'];
            $habitantes = $_POST['habitantes'];
            $superficie = $_POST['superficie'];
            if ($_POST['tieneMetro']){
                $tieneMetro = $_POST['tieneMetro'];
            } else {
                $tieneMetro = 0;
            }
            if(mysqli_select_db($conn, $GLOBALS['db'])) {
            $query = "UPDATE ciudades".
                " SET ciudad='".$ciudad."', pais='".$pais."', habitantes=".$habitantes.", superficie=".$superficie.", tieneMetro =".$tieneMetro."".
                " WHERE id = ".$id."";
                if($conn->query($query) or die($conn->error)){
                    echo
                        "<div class='msg'>". 
                        "<p>Actualización realizada correctamente.</p>".
                        "<a href='./index.php' class='primaryButton'>Volver</a>".
                        "</div>";
                } else {
                    echo
                        "<div class='msg'>". 
                        "<p>Error en la actualización</p>".
                        "<a href='./index.php' class='primaryButton'>Volver</a>".
                        "</div>";
                }
            }
        }

        if(isset($_POST['deleteButton'])){
            if(isset($_POST['radio_group'])){
                $conn = mysqli_connect($GLOBALS['hostname'],$GLOBALS['user'],$GLOBALS['pass']);
                mysqli_select_db($conn, $db);
                $id = $_POST['radio_group'];

                $query = "SELECT * FROM ciudades WHERE id =".$id."";
                $result = $conn-> query($query) or die($conn->error);
                $conn ->close();
                $row = $result->fetch_assoc();
                $ciudad = $row['ciudad'];

                echo 
                    "<div class='msg'>
                        <form action='query.php' method='post'>
                            <p>Esta Seguro que desea eliminar la ciudad ".$ciudad." ?</p>
                            <input type='text' style='display: none;' name='id' value='".$id."'>
                            <a href='./index.php' class='secondaryButton'>Cancelar</a>
                            <button type='submit' class='primaryButton' name='deleteRow'>Aceptar</button>
                        </form>
                    </div>";
            } else {
                echo
                    "<div class='msg'>". 
                    "<p>Debe seleccionar un elemento</p>".
                    "<a href='./index.php' class='primaryButton'>Volver</a>".
                    "</div>";
            }
        }

        if(isset($_POST['deleteRow'])){
            $conn = mysqli_connect($GLOBALS['hostname'],$GLOBALS['user'],$GLOBALS['pass']);
            mysqli_select_db($conn, $db);
            $id = $_POST['id'];
            $query = "DELETE FROM ciudades WHERE id=".$id."";
            if($conn->query($query) or die($conn->error)){
                echo
                    "<div class='msg'>". 
                    "<p>Ciudad eliminada correctamente.</p>".
                    "<a href='./index.php' class='primaryButton'>Volver</a>".
                    "</div>";
            } else {
                echo
                    "<div class='msg'>". 
                    "<p>Error al eliminar la ciudad</p>".
                    "<a href='./index.php' class='primaryButton'>Volver</a>".
                    "</div>";
            }
        }

        if(isset($_POST['addButton'])){
            echo "<div class='createForm' >
                    <h1>Añadir</h1>
                    <form action='query.php' method='post'>
                        <p>Ciudad: <input required type='text' name='ciudad' ></p>
                        <p>País: <input required type='text' name='pais' ></p>
                        <p>Habitantes: <input required type='number' name='habitantes' ></p>
                        <p>Superficie: <input required type='number' step='0.01' name='superficie' ></p>
                        <input type='hidden' name='tieneMetro' value='0'>
                        <p>Tiene Metro: <input type='checkbox' name='tieneMetro' value='1' ></p>
                        <a href='./index.php' class='secondaryButton'>Cancelar</a>
                        <button type='submit' class='primaryButton' name='createRow'>Aceptar</button>
                    </form>
                </div>";
        }

        if(isset($_POST['createRow'])){
            $ciudad = $_POST['ciudad'];
            $pais = $_POST['pais'];
            $superficie = $_POST['superficie'];
            $habitantes = $_POST['habitantes'];
            $tieneMetro = $_POST['tieneMetro'];

            $conn = mysqli_connect($GLOBALS['hostname'],$GLOBALS['user'],$GLOBALS['pass']);
            mysqli_select_db($conn, $db);
            $query="SELECT id FROM ciudades ORDER BY id DESC LIMIT 1";
            $result = $conn->query($query) or die($conn->error);
            $value = $result -> fetch_assoc();
            $id = (int)$value['id'] + 1;
            $query = "INSERT INTO ciudades VALUES (".$id.",'".$ciudad."','".$pais."',".$habitantes.",".$superficie.",".$tieneMetro.")";
            if($conn->query($query) or die($conn->error)){
                echo
                    "<div class='msg'>". 
                    "<p>Ciudad agregada correctamente</p>".
                    "<a href='./index.php' class='primaryButton'>Volver</a>".
                    "</div>";
            } else {
                echo
                    "<div class='msg'>". 
                    "<p>Error en al insertar la ciudad</p>".
                    "<a href='./index.php' class='primaryButton'>Volver</a>".
                    "</div>";
            }
        }
        
    ?>
</body>
</html>