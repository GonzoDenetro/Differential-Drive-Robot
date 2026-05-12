
//--ENCODER VARIABLES
volatile unsigned ticksR = 0;
volatile unsigned ticksL =0;

//Encoder pins
int encoderR = 3;
int encoderL = 2;

//Ticks in disk
int N = 20; 

//MOTOR PINS


//ROBOT PARAMETERS
float L = 0.125; //Meters
float diameter = 0.066; //Meters
float radius = diameter / 2;
float x = 0.0;
float y = 0.0;
float theta = 0.0;
float omegaR = 0.0;
float omegaL = 0.0;

//TIME Variables
unsigned long prevTime = 0;

// ROBOT STATES
enum RobotState {
  FORWARD,
  TURN
};

RobotState state = FORWARD;

float startX = 0.0;
float startY = 0.0;
float targetTheta = 0.0;

// SQUARE TRAJECTORU
int squareSide = 0;
int sideLength = 0.5; // Meters


void setup() {
  // set the encoder pin
  pinMode(encoderL, INPUT);
  //Create Interruption
  attachInterrupt(digitalPinToInterrupt(encoderR), rightEncoderCallback, FALLING);
  attachInterrupt(digitalPinToInterrupt(encoderL), leftEncoderCallback, FALLING);
  //Serial Communication
  Serial.begin(9600);
}


void rightEncoderCallback() {
  ticksR += 1;
}


void leftEncoderCallback() {
  ticksL += 1;
}

void loop() {
  Serial.println(ticksL);
  
}