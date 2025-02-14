<?php
$file = "logins.txt";
if (!file_exists($file)) {
    die("Tidak ada data login.");
}

$logins = file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
foreach ($logins as $index => $login) {
    echo "[$index] $login\n";
}

echo "\nPilih nomor untuk izinkan login atau ketik 'exit': ";
$handle = fopen("php://stdin", "r");
$input = trim(fgets($handle));

if (is_numeric($input) && isset($logins[$input])) {
    $logins[$input] = str_replace("NON AKTIF", "AKTIF", $logins[$input]);
    file_put_contents($file, implode("\n", $logins) . "\n");
    echo "Pengguna telah diizinkan masuk!\n";
} else {
    echo "Keluar atau input tidak valid.\n";
}
?>
