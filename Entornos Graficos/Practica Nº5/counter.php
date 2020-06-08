<?php
    if(isset($_SESSION['contador'])){
        $_SESSION['contador']++;
    } else {
        $_SESSION['contador']=1;
    }
?>