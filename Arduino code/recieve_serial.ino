float dist=0;
float angle=0;
int start=0;
int quality=0;
String data="";
char c;

void setup() {
 
  Serial.begin(115200); 
  
}



void loop() {
  // put your main code here, to run repeatedly:
  
while(Serial.available()>0)
{
  c=Serial.read();
  if(c=='\n')
  break;
  else
  data=data+c;
  
}
if(c=='\n')
{
Serial.println(data);
data="";
c=0;
}
}
