import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="omar",
  database="Fishfarms"

)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE Fishfarms")
#mycursor.execute("CREATE TABLE sensors (id INT AUTO_INCREMENT PRIMARY KEY,TEMP INT(5),DO INT(5),PH INT(5),ORP INT(5))") 
#mycursor.execute("ALTER TABLE sensors Change name temperature VARCHAR(255) ")
#mycursor.execute("DROP TABLE sensors") 



sql = "INSERT INTO sensors (TEMP,DO,PH,ORP) VALUES (%s,%s,%s,%s)"
val = [
  (21,2,7,114),
  (20,1,5,111),
  (22,3,6,112),
  (23,5,8,112)
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.") 

#echo "id: " . $row["id"]. " - Temp: " . $row["TEMP"]. " - Dissolved Oxygen: " . $row["DO"]. " - PH: " . $row["PH"]. " - ORP: " . $row["ORP"]. "<br>";

$s1=$row["TEMP"];
        $s2=$row["DO"];
        $s3=$row["PH"];
        $s4=$row["ORP"];
