<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
    <?php
        require('connection.php');
        
        $sql = 'SELECT * FROM buscador WHERE canciones LIKE "%'.$_POST['search'].'%"';
        $result = $conn->query($sql) or die($conn->error);
        if(mysqli_num_rows($result)==0){
            echo "<p class='no-results'>No se encontraron resultados para su búsqueda.</p>";
        } else {
    ?>
    <nav class="navbar navbar-light bg-light">
        <div class="container">
          <a class="navbar-brand" href="#">
            <img src="icons/music_icon.png" width="30" height="30" class="d-inline-block align-top" alt="" loading="lazy">
            Buscador de Canciones
          </a>
        </div>
    </nav>
    <br>
    <div class="container">
        <table class="table table-hover">
            <thead class="thead-dark">
                <th scope="col">Canción</th>
            </thead>
            <tbody>
    <?php
            while($row = $result->fetch_assoc()){
    ?>
            <tr>
                <td><?php echo $row['canciones']; ?></td>
            </tr>
    <?php
            }
    ?>
            </tbody>
            <tfoot>
                <td class="bg-info">Numero de Resultados: <?php echo mysqli_num_rows($result)?></td>
            </tfoot>
        </table>
    </div>
    <?php
        }
    ?>
    <div class="container">
        <a class="btn btn-link" href="http://localhost/Codigos/Practica%207/Ejercicio%208">Volver al buscador</a>
    </div>

</body>
</html>