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
#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11);
int flag = 0 ; 
void setup() {
  // initialize both serial ports:
  Serial.begin(9600);
  Serial1.begin(9600);
  Serial2.begin(9600);
  Serial3.begin(9600);
mySerial.begin(9600);
  pinMode(13,OUTPUT);
  
  
  delay(1000);
  
Serial.print("C,1");
Serial.print('\r');
Serial1.print("C,1");
Serial1.print('\r');
Serial2.print("C,1");
Serial2.print('\r');
Serial3.print("C,1");
Serial3.print('\r');
delay(10);
}
void loop() {
  // read from port 1, send to port 0:
  String omar = "" ;
char s = ' ' ;

 
 
 




  while (s !='\r')
   {
     if(Serial1.available())
     {
   s = Serial1.read();
   if(s !='ÿ')
   omar = omar + s ;
   }
   }
      Serial.print("a ");

   Serial.println(omar);
   omar="";
   s=' ';
   delay(1000);





  while (s !='\r')
   {
     if(Serial2.available())
     {
   s = Serial2.read();
   if(s !='ÿ')
   omar = omar + s ;
   }
   }
   Serial.print("b ");
   Serial.println(omar);
   omar="";
   s=' ';
   delay(1000);





  while (s !='\r')
   {
     if(Serial3.available())
     {
   s = Serial3.read();
   if(s !='ÿ')
   omar = omar + s ;
   }
   }
   Serial.print("c ");
   Serial.println(omar);
   omar="";
   s=' ';
   delay(1000);


    while (s !='\r')
   {
     if(mySerial.available())
     {
   s = mySerial.read();
   if(s !='ÿ')
   omar = omar + s ;
   }
   }
   Serial.print("d ");
   Serial.println(omar);
   omar="";
   s=' ';
   delay(1000);

}
