<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practica 7 - Ejercicio 7</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
    <?php
        require('data.php'); 
    ?>
    <div class="container">
        <nav class="navbar navbar-light bg-light">
            <a class="navbar-brand" href="#">
                <img src="icons/store_icon.png" width="30" height="30" class="d-inline-block align-top" alt="Shopping icon" loading="lazy">
                Productos
            </a>
            <form action="cart.php" method="get">
                <button class="btn">
                    <img src="icons/cart_icon.png" width="30" height="30" class="d-inline-block align-top" alt="Shopping icon" loading="lazy">
                </button>
            </form>
        </nav>
    </div>
    <?php
        if($products){
            while($row = $result->fetch_assoc()){
    ?>
        <div class="container">
            <div class="card">
                <div class="card-body">
                    <div class="row">
                        <div class="col">
                            <label for="product">Descripción</label>   
                            <h5 class="card-title" id="product"><?php echo $row['producto']?></h2>
                        </div>
                        <div class="col">
                            <label for="price">Precio</label>   
                            <h6 class="card-text" id="price">$<?php echo $row['precio']?></h3>
                        </div>
                    <form action="cart.php" method="post">
                        <input type="hidden" name="id" value="<?php echo $row['id']?>">
                        <input type="hidden" name="product" value="<?php echo $row['producto']?>">
                        <input type="hidden" name="price" value="<?php echo $row['precio']?>">
                            <div class="col">
                                <label for="quantity">Cantidad</label>   
                                <input type="number" name="quantity" id="quantity" class="form-control" required>
                            </div>
                    </div>
                        <div class="row justify-content-end">
                            <div class="col align-self-end">
                                <button type="submit" name="addToCart"  class="btn btn-outline-primary btn-sm">Add</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    <?php
            }
        } else {
    ?>
        <div class="no-products">
            <p>No hay productos cargados</p>
        </div>
    <?php
        }
    ?>
</body>
</html>