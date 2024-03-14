<?php

$conn = new mysqli("localhost", "root", "", "giochino");

if ($conn->connect_error) {
    die("Connessione al database fallita: " . $conn->connect_error);
}






// Esempio: restituzione solo dell'ID dell'utente
function getUser() {
    global $conn;
    $sql = "SELECT id FROM users"; // Query per ottenere tutti gli ID degli utenti
    $result = $conn->query($sql);

    $ids = '';
    // Estrai gli ID dalla query e aggiungili alla stringa
    while ($row = $result->fetch_assoc()) {
        $ids .= $row['id'] . ',';
    }

    // Rimuovi l'ultima virgola
    $ids = rtrim($ids, ',');

    // Restituisci gli ID come una stringa separata da virgole
    return $ids;
}



// Funzione per ottenere un altro dato da un'altra tabella
function getOtherData() {
    global $conn;
    $sql = "SELECT nome FROM altre_tabella LIMIT 1"; // Esempio di query su un'altra tabella
    $result = $conn->query($sql);
    $row = $result->fetch_assoc();
    return $row['nome'];
}

// Gestisci la richiesta AJAX
if (isset($_GET['action'])) {
    $action = $_GET['action'];

    // Esegui l'operazione richiesta
    switch ($action) {
        case 'getUser':
            echo getUser();
            break;
        case 'getOtherData':
            echo getOtherData();
            break;
        default:
            echo "Azione non valida";
            break;
    }
}

// Chiudi la connessione al database
$conn->close();









/*
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
    */





 