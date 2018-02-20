#define RED 4
#define GREEN 3
#define MAG A3
#define ANGLE A5

void setup(){
  Serial.begin(9600);
  pinMode(RED, OUTPUT);
  pinMode(GREEN, INPUT);
}
void loop(){
  if(Serial.available()>0){
    char c = Serial.read();
    switch(c){
      case 'p':
        Serial.print(analogRead(ANGLE));
        Serial.print(",");
        Serial.println(analogRead(MAG));
        break;
      case 'r':
        digitalWrite(RED,HIGH);
        digitalWrite(GREEN,LOW);
        break;
      case 'g':
        digitalWrite(RED,LOW);
        digitalWrite(GREEN,HIGH);
        break;
    }
  }
}
