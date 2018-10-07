    ;int kd = 0;
    ;int kdALT = 0;
    ;int stat = 0;
    ;int dif;
    ;int x = 1;
    ;float s;
    // defines pins numbers
    const int trigPin = 10;
    const int echoPin = 11;
    // defines variables
    long duration;
    int distance;

    
    void setup() {
    pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
    pinMode(echoPin, INPUT); // Sets the echoPin as an Input
    pinMode(2, OUTPUT);
    Serial.begin(9600); // Starts the serial communication
    }


    void reading(){
    // Clears the trigPin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);
    // Calculating the distance
    distance= duration*0.034/2;
    }

    // checking sensor
    void loop() {
    reading();

    kd = 0.8 * kd + 0.2 * distance;
    
    dif = abs(kd - kdALT);
    if (dif <= 1){
      stat = 0;
      Serial.println(stat);
      delay(100);
      }
     else {
      while (x == 0){
        stat = 1;
        digitalWrite(2, HIGH);
        Serial.println(stat);
        delay(1000);
        digitalWrite(2, LOW);
        x++;
        }
        }
        if (kd == kdALT){
          x = 0;
          }
          
      kdALT = kd;
    }
