/**
 * Simple Read
 * 
 * Read data from the serial port and change the color of a rectangle
hen a switch connected to a Wiring or Arduino board is pressed and released.
 * This example works with the Wiring / Arduino program that follows below.
 */
  
import processing.net.*;


import processing.serial.*;
Client myClient; 

Serial myPort;  // Create object from Serial class
char val;      // Data received from the serial port
char omar[] ={'a','a','a','a','a','a','a','a','a','a','a','a','a','a','a'};
String omar1 ; 
void setup() 
{
  size(200, 200);
  // I know that the first port in the serial list on my mac
  // is always my  FTDI adaptor, so I open Serial.list()[0].
  // On Windows machines, this generally opens COM1.
  // Open whatever port is the one you're using.
  String portName = Serial.list()[0];
  myPort = new Serial(this, "/dev/ttyACM0", 9600);
    myClient = new Client(this, "", 50007); 

}
String xx="";
void draw()
{
  for ( int i = 0 ; i<=9 ; i++)
  omar[i]='z';
    // println("KK");

   //  println(omar[0]);

  omar1="";
  val='c';
  int j=0;
  int uu=0;
  while(val!='\r'&&uu<2)
  {
  if ( myPort.available() > 0) {  // If data is available,
    val = myPort.readChar();         // read it and store it in val
    
    if(val!='\n')
    {
      if(val=='.')
      uu++;
      if(uu<2)
      {
    omar1=omar1+val;
    omar[j]=val;
    j++;
      }
    }
    
  }
  
  println("read");

  }
    // println("YY");

   //  println(omar[0]);

  //   println(omar);
      

  if(omar[0]=='a'||omar[0]=='b'||omar[0]=='c'||omar[0]=='d')
  {
 println(omar1);
  println("/");
  
  myClient.write(omar1);
    delay(50);

  }
  
  //if(omar[0] == 'a')
  
  //if(omar[0] == 'b')
  //if(omar[0] == 'c')
  //if(omar[0] == 'd')
 
}


String omar()
{
  int j = 0 ;
  String k="";
  for(j=0;j<=6;j++)
  {
    if(omar[j+2]!='z')
    k=k+omar[j];
    else
    break;
  }
  return k ;
}

/*

// Wiring / Arduino Code
// Code for sensing a switch status and writing the value to the serial port.
int switchPin = 4;                       // Switch connected to pin 4

void setup() {
  pinMode(switchPin, INPUT);             // Set pin 0 as an input
  Serial.begin(9600);                    // Start serial communication at 9600 bps
}

void loop() {
  if (digitalRead(switchPin) == HIGH) {  // If switch is ON,
    Serial.write(1);               // send 1 to Processing
  } else {                               // If the switch is not ON,
    Serial.write(0);               // send 0 to Processing
  }
  delay(100);                            // Wait 100 milliseconds
}

*/
