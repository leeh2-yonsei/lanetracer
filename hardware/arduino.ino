// 모터 A
#define IN3 9
#define IN4 8
#define ENB 10  // PWM 핀

// 모터 B
#define IN1 7
#define IN2 6
#define ENA 5   // PWM 핀

int speedVal = 90;  // 속도: 0~255
int angle = -10;
char command;
int time = 250;

// -------- 함수 선언 --------
void goForward();
void turnLeft();
void turnRight();
void stopMotors();
// --------------------------

void setup() {
  Serial.begin(9600);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  analogWrite(ENA, speedVal);
  analogWrite(ENB, speedVal);
}

void loop() {

  if (Serial.available() > 0) {
    angle = Serial.parseInt();

  if (angle < 0) command = '3';
  else if (angle == 0) command = 's';
  else if (angle > 0 && angle < 20) command = '0';
  else if (angle >= 20 && angle < 40) command = '1';
  else if (angle >= 40 && angle < 80) command = '2';
  else if (angle >= 80 && angle < 100) command = '4';
  else if (angle >= 100 && angle < 120) command = '5';
  else if (angle >= 120 && angle < 140) command = '6';
  else if (angle >= 140 && angle < 160) command = '7';
  else if (angle >= 160 && angle <= 180) command = '8';
  else command = 's';

  switch (command) {
    case '0':
      turnLeft(10);
      break;

    case '1':
      turnLeft(5);      
      break;

    case '2':
      turnLeft(2);
      break;

    case '3':
      goBack();
      break;

    case '4':
      goForward();
      break;

    case '5':
      turnRight(2);
      break;

    case '6':
      turnRight(5);
      break;

    case '7':
      turnRight(10);
      break;

    case '8':
      turnRight(20);
      break;

    case 's':
      stopMotors();
      break;

    default:
      stopMotors();
      break;
  }
  }
}

// ---- 함수 정의 ----
void goForward() {
  analogWrite(ENA, speedVal-10);
  analogWrite(ENB, speedVal-10);

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void goBack() {
  analogWrite(ENA, speedVal-2);
  analogWrite(ENB, speedVal-10);

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void turnLeft(int speed_ctrl) {
  analogWrite(ENA, speedVal+speed_ctrl);
  analogWrite(ENB, speedVal-speed_ctrl);

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void turnRight(int speed_ctrl) {
  analogWrite(ENA, speedVal-speed_ctrl);
  analogWrite(ENB, speedVal+speed_ctrl);

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void stopMotors() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}
