
//ENCODER VARIABLES
volatile unsigned currentTickR = 0;
volatile unsigned previousTickR =0;
volatile unsigned deltaTickR = 0;

int encoderR = 3;

void setup() {
  //Create Interruption
  attachInterrupt(digitalPinToInterrupt(encoderR), rightEncoderCallback, FALLING);

  //Serial Communication
  Serial.begin(9600);
}


void rightEncoderCallback() {
  deltaTickR = currentTickR - previousTickR;
  previousTickR = currentTickR;  
}


void loop() {
  //Time Elapsed
  currentTickR = millis();

  Serial.println(deltaTickR);

}