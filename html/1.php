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
echo "Connected successfully";


$sql = "SELECT * FROM sensors";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Temp: " . $row["TEMP"]. " - Dissolved Oxygen: " . $row["DO"]. " - PH: " . $row["PH"]. " - ORP: " . $row["ORP"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
