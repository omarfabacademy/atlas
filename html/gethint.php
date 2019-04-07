

<?php
$servername = "localhost";
$username = "root";
$password = "omar";
$dbname = "Fishfarms";
// Create connection
$conn = new mysqli($servername, $username, $password,$dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
//echo "Connected successfully";

$sql = "SELECT * FROM sensors ORDER BY id DESC LIMIT 1";
$result = $conn->query($sql);

    $row = $result->fetch_assoc();
        echo $row["TEMP"];
  
$conn->close();

?> 
