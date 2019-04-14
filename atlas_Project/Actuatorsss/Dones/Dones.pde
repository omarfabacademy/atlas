/**
 * Shared Drawing Canvas (Client) 
 * by Alexander R. Galloway. 
 * 
 * The Processing Client class is instantiated by specifying a remote 
 * address and port number to which the socket connection should be made. 
 * Once the connection is made, the client may read (or write) data to the server.
 * Before running this program, start the Shared Drawing Canvas (Server) program.
 */


import processing.net.*;
import processing.serial.*;

Serial myPort;  // Create object from Serial class
int val;       

Client c;
String input;
int data[]={0};


void setup() 
{
  size(200, 200);

  c = new Client(this, "127.0.0.1", 12345); // Replace with your server's IP and port
  String portName = Serial.list()[0];
  myPort = new Serial(this, portName, 9600);
}

void draw() 
{
   background(255);             // Set background to white
  if (data[0] == 0) {              // If the serial value is 0,
    fill(0);                   // set fill to black
  } 
  else {                       // If the serial value is not 0,
    fill(204);                 // set fill to light gray
  }
  rect(50, 50, 100, 100);
  // Receive data ana from server
  if (c.available() > 0) {
    input = c.readString();
    data = int(split(input, ' ')); // Split values into an array
    myPort.write(input);              // send an H to indicate mouse is over square

    
  }
}
