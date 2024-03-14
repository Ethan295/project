<?php
session_start(); // Avvia la sessione
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 20px;
        background-color: #f4f4f4;
        color: #333;
    }

    .user-info {
        text-align: right;
        margin-bottom: 20px;
    }

    .logout {
        color: #e74c3c;
        cursor: pointer;
    }

    form {
        background-color: #fff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }

    input[type="text"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 15px;
        box-sizing: border-box;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    input[type="submit"] {
        background-color: #3498db;
        color: #fff;
        padding: 12px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-weight: bold;
    }

    input[type="submit"]:hover {
        background-color: #2980b9;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        background-color: #fff;
        padding: 20px;
        margin-bottom: 15px;
        border-radius: 8px;
        box-shadow: 0 0 8px rgba(0, 0, 0, 0.1);
    }

    li p {
        margin: 0;
        font-size: 16px;
    }

    .no-content {
        text-align: center;
        color: #555;
        margin-top: 20px;
    }
    </style>
</head>

<body>

    <div class="user-info">
        <?php
        if (isset($_SESSION['username'])) {
            echo "Benvenuto, " . $_SESSION['username'] . "!";
        }
        ?>
        <br>
        <span class="logout" onclick="logout()">Logout</span>
    </div>

    <form action="feed-logic.php" method="post">
        <input type="text" name="contenuto" id="contenuto" placeholder="Inserisci il tuo messaggio qui" required>
        <br>
        <input type="submit" name="invia" value="Invia">
    </form>

    <ul>
        <?php
        $conn = new mysqli("localhost", "root", "", "feed");

        $sql = "SELECT * FROM paginafeed";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                echo "<li><p>" . "Numero Post: " . $row['id'] . "<br>" . "Nome Utente: " . $row['username'] . "<br>" . "Messaggio: " . $row['messaggio'] . "</p></li>";
            }
        } else {
            echo "<p class='no-content'>Nessun contenuto nella tabella 'paginafeed'.</p>";
        }

        $conn->close();
        ?>
    </ul>

    <script>
    function logout() {
        window.location.href = 'logout.php';
        
    }
    </script>
</body>

</html>