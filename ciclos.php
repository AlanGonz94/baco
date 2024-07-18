<?php
// Configurar una cookie
setcookie("usuario", "Juan", time() + (86400 * 30), "/"); // 86400 = 1 dia
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Cookie Test</title>

</head>

<body>
    <h1>Cookie Set</h1>
        <?php
        // verificar si la cookie esta configurada
        if (isset($_COOKIE["usuario"])) {
            echo "Cookie 'usuario' esta configurada. Valor: " . 
    $_COOKIE["usuario"];
        } else {
            echo "Cookie 'usuario' no esta configurada,";
        }
        ?>
</body>
</html>