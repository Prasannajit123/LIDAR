#include <RPLidar.h>
#include<SoftwareSerial.h>
RPLidar lidar;
SoftwareSerial myserial(2,3);
#define RPLIDAR_MOTOR 5       
void setup() {
   myserial.begin(115200);
   Serial.begin(115200);
  // bind the RPLIDAR driver to the arduino hardware serial
  lidar.begin(Serial);
   
  // set pin modes
  pinMode(RPLIDAR_MOTOR, OUTPUT);
}
void loop() {
  if (IS_OK(lidar.waitPoint())) {
    float distance = lidar.getCurrentPoint().distance; //distance value in mm unit
    float angle    = lidar.getCurrentPoint().angle; //anglue value in degree
    bool  startBit = lidar.getCurrentPoint().startBit; //whether this point is belong to a new scan
    byte  quality  = lidar.getCurrentPoint().quality; //quality of the current measurement
     
    //perform data processing here... 
     if((angle>=0)&(angle<=180)&(quality>0)&(distance<5000))
   {
     myserial.print(distance);       
    myserial.print("A");  
     myserial.print(angle);       
     myserial.print("B"); 
    myserial.print(startBit);       
     myserial.print("C"); 
      myserial.print(quality);       
     myserial.println("D"); 
  }
    /*
       myserial.print(distance);       
    myserial.print(" ");  
     myserial.print(angle);       
     myserial.print(" "); 
    myserial.print(startBit);       
     myserial.print(" "); 
      myserial.print(quality);       
     myserial.println(" "); 
    */
 

    
  } else {
    analogWrite(RPLIDAR_MOTOR, 0); //stop the rplidar motor
     
    // try to detect RPLIDAR... 
    rplidar_response_device_info_t info;
    if (IS_OK(lidar.getDeviceInfo(info, 100))) {
       // detected...
       lidar.startScan();
        
       // start motor rotating at max allowed speed
       analogWrite(RPLIDAR_MOTOR, 255);
       delay(1000);
    }
  }
}
