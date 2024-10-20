// #include <Stepper.h>

// const int stepsPerRevolution = 200;
// const int mm = 1600;

// // initialize the stepper library on pins 8 through 11:
// Stepper myStepper0(stepsPerRevolution, 2, 3);
// Stepper myStepper(stepsPerRevolution, 8, 9);

// void setup() {
//   Serial.begin(9600);
//   myStepper.setSpeed(200);
// }

// void loop() {
//   while (Serial.available() == 0) {}

//   if (Serial.readString() == "start\n") {
//     myStepper.step(160);
//   }
// }

#include <Stepper.h>

const int stepsPerRevolution = 200;
const int mm = 1600;

// initialize the stepper library on pins 8 through 11:
Stepper myStepper1(stepsPerRevolution, 8, 9);
Stepper myStepper2(stepsPerRevolution, 2, 3);

void setup() {
  Serial.begin(9600);
  myStepper1.setSpeed(200);
  myStepper2.setSpeed(200);
}

void loop() {
  while (Serial.available() == 0) {}
  // String input = Serial.readString();
  // Serial.println(input.charAt(0));
  // Serial.println(input.substring(1, input.length() - 1));

  char dir = (char) Serial.read();
  // Serial.println(Serial.parseFloat());
  int steps = Serial.parseFloat() * mm;
  Serial.readString();

  switch (dir) {
    case 'u':
      myStepper2.step(-steps);
      break;
    case 'r':
      myStepper1.step(-steps);
      break;
    case 'd':
      myStepper2.step(steps);
      break;
    case 'l':
      myStepper1.step(steps);
      break;
  }
}
