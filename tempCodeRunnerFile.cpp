int ledPin = 13;
int buttonPin = 7;
int sensorValue = 0;

void setup(){
    pinMode(ledPin,OUTPUT);
    pinMode(buttonPin,INPUT);
    Serial.begin(9600);
}
void loop(){
    int buttonState = digitalRead(buttonPin);
    if (buttonState == HIGH){
        digitalWrite(ledPin,HIGH);
        Serial.println("Button Pressed - LED ON");
    }
    else{
        digitalWrite(ledPin,LOW);
        Serial.println("LED off");
    }
    sensorValue = analogRead(A0);
    Serial.print("Sensor Value: ");
    Serial.println(sensorValue);

    delay(500);
}