#include <SoftwareSerial.h>      //we have to include the SoftwareSerial library, or else we can't use it.  
#define rx 2                     //define what pin rx is going to be.
#define tx 3                     //define what pin Tx is going to be.

SoftwareSerial myserial(rx, tx); //define how the soft serial port is going to work.



char ph_data[20];                  //we make a 20 byte character array to hold incoming data from the pH.
char computerdata[20];             //we make a 20 byte character array to hold incoming data from a pc/mac/other.
byte received_from_computer=0;     //we need to know how many characters have been received.                                
byte received_from_sensor=0;       //we need to know how many characters have been received.
byte arduino_only=0;               //if you would like to operate the pH Circuit with the Arduino only and not use the serial monitor to send it commands set this to 1. The data will still come out on the serial monitor, so you can see it working.  
byte startup=0;                    //used to make sure the Arduino takes over control of the pH Circuit properly.
float ph=0;                        //used to hold a floating point number that is the pH.
byte string_received=0;            //used to identify when we have received a string from the pH circuit.


void setup(){
  
     Serial.begin(9600);          
     myserial.begin(9600);      
    
     if(startup==0){                
          myserial.print("c,0\r");  
          Serial.print("Omar 1");
          delay(50);                
          myserial.print("c,0\r");
                    Serial.print("Omar 2");
          delay(50);                
          startup=1;              
       }
      }
  
 
 void serialEvent(){            
        if(arduino_only==0){      
           received_from_computer=Serial.readBytesUntil(13,computerdata,20); 
                     Serial.print("Omar 3");
           computerdata[received_from_computer]=0;
           myserial.print(computerdata);          
           myserial.print('\r');                  
          }    
        }
 
 
  

void loop(){
    
     received_from_sensor=myserial.readBytesUntil(13,ph_data,20);
     ph_data[received_from_sensor]=0;  
     string_received=1;              
     Serial.println(received_from_sensor);              
   
  
 
 
  
 }      


void cal_s(){                        //calibrate to a pH of 7
  myserial.print("cal,mid,7\r");}    //send the "cal,mid,7" command to calibrate to a pH of 7.00


void cal_f(){                       //calibrate to a pH of 4
  myserial.print("cal,low,4\r");}     //send the "cal,low,4" command to calibrate to a pH of 4.00


void cal_t(){                      //calibrate to a pH of 10.00
  myserial.print("cal,high,10\r");}  //send the "cal,high,10" command to calibrate to a pH of 10.00  


void phFactoryDefault(){           //factory defaults the pH circuit
  myserial.print("X\r");}          //send the "X" command to factory reset the device


void read_info(){                  //get device info
    myserial.print("I\r");}        //send the "I" command to query the information


void phSetLEDs(byte enabled)      //turn the LEDs on or off
{
  if(enabled)                     //if enabled is > 0
    myserial.print("L,1\r");      //the LED's will turn ON
  else                            //if enabled is 0        
    myserial.print("L,0\r");      //the LED's will turn OFF
}

