<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carro de Compras</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>   
<div class="container">
        <nav class="navbar navbar-light bg-light">
            <a class="navbar-brand" href="http://localhost/Codigos/Practica%207/Ejercicio%207/">
                <img src="icons/cart_icon.png" width="30" height="30" class="d-inline-block align-top" alt="Shopping icon" loading="lazy">
                Carrito de Compras
            </a>
    </div>
    <?php
    session_start();
    $_SESSION['total']=0;
    if(isset($_SESSION['cart'])){
        $cart = $_SESSION['cart'];
    } else{
        $cart=[];
    }
    if(isset($_POST['addToCart'])){
        $product = array ( 
            'id' => $_POST['id'],
            'product' => $_POST['product'],
            'price' => $_POST['price'],
            'quantity' => $_POST['quantity'],
        );
        $id = md5($product['id']);
        if(array_key_exists($id,$cart)){
            $prod = $cart[$id];
            $prod['quantity'] = $prod['quantity'] + $_POST['quantity'];
            $cart[$id]=$prod;
        } else {
            $cart[$id]=$product;
        }
        $_SESSION['cart'] = $cart;
    }
    if(isset($_POST['deleteFromCart'])){
        $id = md5($_POST['id']);
        unset($cart[$id]);
        $_SESSION['cart']=$cart;
    }
    
    if(count($cart)==0){
        ?>
        <div class="container">
            <div class="card">
                <h5 class="card-description">No hay productos cargados en el carrito.</h5>
            </div>
        </div>
        <?php
    } else {
        foreach($cart as $product){
            $_SESSION['total'] = $_SESSION['total'] + $product['price'] * $product['quantity'];
            ?>
        <div class="container">
            <div class="card">
                <div class="card-body">
                    <div class="row">
                        <div class="col">
                            <p class="card-title"><?php echo $product['product']?></p>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-5">
                            <p class="card-description">Precio Unitario: <?php echo $product['price']?></p>
                        </div>
                        <div class="col-5">
                            <p class="card-description">Cantidad: <?php echo $product['quantity']?></p>
                        </div>
                        <div class="col">
                            <form action="<?php echo $_SERVER['PHP_SELF']?>" method="post">
                                <input type="hidden" name="id" value="<?php echo $product['id']?>">
                                <button type="submit" name="deleteFromCart" class="btn"><img src="icons/delete_icon.png" width="30" height="30" class="d-inline-block align-top" alt="Delete icon" loading="lazy"></button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <?php
        }
    }
    ?>
    <div class="container">
        <div class="card">
            <div class="card-header">
                Total: $<?php echo $_SESSION['total']?>
            </div>
        </div>
    </div>
    <div class="container">
        <a href="http://localhost/Codigos/Practica%207/Ejercicio%207/" class="btn btn-link">Volver a la página principal</a>
    </div>
    </body>
    </html>