<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['nome'] ? htmlentities($_POST['nome']) : '';
    $password = $_POST['password'] ? htmlentities($_POST['password']) : '';

    $conn = new mysqli("localhost", "root", "", "feed");

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Controllo se lo username esiste già nel database
    $checkSql = "SELECT * FROM userdata WHERE username = ?";
    $checkStmt = $conn->prepare($checkSql);
    $checkStmt->bind_param("s", $username);
    $checkStmt->execute();
    $checkResult = $checkStmt->get_result();

    if ($checkResult->num_rows > 0) {
        // Lo username esiste già
        $_SESSION['error_message'] = "Lo username esiste già, scegli un altro.";
        $checkStmt->close();
        $conn->close();
        header("Location: register_view.php");
        exit;
    }

    // Generazione di un numero casuale di otto caratteri (int)
    $salt = mt_rand(10000000, 99999999);

    // Aggiunta del salt alla password prima della cifratura con SHA-256
    $hashedPassword = hash('sha256', $password . $salt);

    // Utilizzo di prepared statement per prevenire SQL injection
    $stmt = $conn->prepare("INSERT INTO userdata (username, password, salt) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $username, $hashedPassword, $salt);
    $stmt->execute();
    $stmt->close();

    // Inserimento nel database avvenuto con successo
    $_SESSION['success_message'] = "Registrazione avvenuta con successo.";
    $conn->close();
    header("Location: login_view.php");
    exit;
}


/*
Non reversibilità: È impossibile risalire ai dati originali dall'hash.

Collision Resistance: È difficile trovare due input diversi che producono lo stesso hash.

Avalanche Effect: Anche una piccola modifica all'input genera un hash completamente diverso.

Ampia applicabilità: Può essere usato in molte situazioni diverse, dalla sicurezza informatica alla crittografia delle password

A.C.H sono dispendiosi a livello computazionale
*/
?>
