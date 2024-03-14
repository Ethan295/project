<?php
session_start(); // Avvia la sessione

$contenuto = isset($_POST['contenuto']) ? htmlentities($_POST['contenuto']) : '';
$username = isset($_SESSION['username']) ? $_SESSION['username'] : '';

$conn = new mysqli("localhost", "root", "", "feed");

$sql = "INSERT INTO paginafeed VALUES (default,'$username','$contenuto')";
$conn->query($sql);

header("Location: feed-view.php");
?>
