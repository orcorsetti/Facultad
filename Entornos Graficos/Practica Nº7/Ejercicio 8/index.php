<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practica 7 -Ejercicio 8</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
    <nav class="navbar navbar-light bg-light">
        <div class="container">
          <a class="navbar-brand" href="#">
            <img src="icons/music_icon.png" width="30" height="30" class="d-inline-block align-top" alt="" loading="lazy">
            Buscador de Canciones
          </a>
        </div>
    </nav>
    <nav class="navbar navbar-light bg-light">
        <div class="container">
            <form class="form-inline" action="search.php" method="post">
                <input required class="form-control" type="search" placeholder="Search" name="search" maxlength="50" aria-label="Search">
                <button class="btn" type="submit"><img src="icons/search_icon.png"  width="30" height="30" class="d-inline-block align-top" alt="search icon" loading="lazy"></button>
            </form>
        </div>
    </nav>
</body>
</html>