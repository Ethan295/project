<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .login-container {
        background-color: #fff;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        text-align: center;
    }

    h2 {
        color: #333;
    }

    form {
        margin-top: 20px;
    }

    label {
        display: block;
        margin-bottom: 8px;
        color: #333;
    }

    input {
        width: 100%;
        padding: 8px;
        margin-bottom: 16px;
        box-sizing: border-box;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    input[type="submit"] {
        background-color: #4caf50;
        color: #fff;
        cursor: pointer;
    }

    input[type="submit"]:hover {
        background-color: #45a049;
    }

    p {
        color: red;
        text-align: center;
    }
    </style>
</head>

<body>
    <div class="login-container">

    <a href="register_view.php" style="float: left;">Register</a>

        <h2>Login</h2>

        <?php   
        session_start();
        if (isset($_SESSION['error_message'])) {
            echo "<p>".$_SESSION['error_message']."</p>";
            unset($_SESSION['error_message']);
        }
        ?>


        <form action="login_logic.php" method="post">
            <label for="nomeLogin">Nome Utente:</label>
            <input type="text" id="nomeLogin" name="nomeLogin" required>

            <label for="passwordLogin">Password:</label>
            <input type="password" id="passwordLogin" name="passwordLogin" required>

            <input type="submit" value="Accedi">
        </form>
    </div>
</body>

</html>