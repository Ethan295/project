<?php
session_start(); // Avvia la sessione

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $nomeLog = $_POST['nomeLogin'];
    $passwordLog = $_POST['passwordLogin'];

    $conn = new mysqli("localhost", "root", "", "feed");

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SELECT * FROM userdata WHERE username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $nomeLog);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $salt = $row['salt'];
        $hashedPassword = hash('sha256', $passwordLog . $salt);

        if ($row['password'] == $hashedPassword) {
            // Imposta la variabile di sessione per l'username
            $_SESSION['username'] = $nomeLog;
            $_SESSION['logged_in'] = true;
            $stmt->close();
            $conn->close();
            header("Location: feed-view.php");
            exit;
        }
    }

    $_SESSION['logged_in'] = false;
    $_SESSION['error_message'] = "Credenziali errate";
    $stmt->close();
    $conn->close();
    header("Location: login_view.php");
    exit;
}

?>
