/*
  Mega multple serial test
 
 Receives from the main serial port, sends to the others. 
 Receives from serial port 1, sends to the main serial (Serial 0).
 
 This example works only on the Arduino Mega
 
 The circuit: 
 * Any serial device attached to Serial port 1
 * Serial monitor open on Serial port 0:
 
 created 30 Dec. 2008
 modified 20 May 2012
 by Tom Igoe & Jed Roach
 
 This example code is in the public domain.
 
 */

int flag = 0 ; 
void setup() {
  // initialize both serial ports:
  Serial.begin(9600);

  pinMode(13,OUTPUT);
  
  
  delay(100);
  
Serial.print("C,1");
Serial.print('\r');
delay(10);
}
void loop() {
  // read from port 1, send to port 0:
  String omar = " " ;
char s = ' ' ;

 
 
   while (s !='\r')
   {
     if(Serial.available())
     {
   s = Serial.read();
   if(s !='ÿ')
   omar = omar + s ;
   }
   }
   Serial.println(omar);
   omar=" ";
   s=' ';
   delay(1000);

}
