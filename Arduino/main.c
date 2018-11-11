const int INPUT_00 = 0;
const int INPUT_01 = 1;
const int INPUT_02 = 2;
const int INPUT_03 = 3;
const int INPUT_04 = 4;
const int INPUT_05 = 5;

const int OUTPUT_00 = 14;
const int OUTPUT_01 = 15;
const int OUTPUT_02 = 16;
const int OUTPUT_03 = 17;
const int OUTPUT_04 = 18;
const int OUTPUT_05 = 19;

int val_00 = 0;
int val_01 = 0;
int val_02 = 0;
int val_03 = 0;
int val_04 = 0;
int val_05 = 0;

void setup()
{
  pinMode(INPUT_00, INPUT);
  pinMode(INPUT_01, INPUT);
  pinMode(INPUT_02, INPUT);
  pinMode(INPUT_03, INPUT);
  pinMode(INPUT_04, INPUT);
  pinMode(INPUT_05, INPUT);
  
  pinMode(OUTPUT_00, OUTPUT);
  pinMode(OUTPUT_01, OUTPUT);
  pinMode(OUTPUT_02, OUTPUT);
  pinMode(OUTPUT_03, OUTPUT);
  pinMode(OUTPUT_04, OUTPUT);
  pinMode(OUTPUT_05, OUTPUT);

  digitalWrite(OUTPUT_00, LOW);
  digitalWrite(OUTPUT_01, LOW);
  digitalWrite(OUTPUT_02, LOW);
  digitalWrite(OUTPUT_03, LOW);
  digitalWrite(OUTPUT_04, LOW);
  digitalWrite(OUTPUT_05, LOW);
}

void loop()
{
  val_00 = digitalRead(INPUT_00);
  if(val_00 == HIGH){
    digitalWrite(OUTPUT_00, HIGH);
  }else{
    digitalWrite(OUTPUT_00, LOW);
  }
  
  val_01 = digitalRead(INPUT_01);
  if(val_01 == HIGH){
    digitalWrite(OUTPUT_01, HIGH);
  }else{
    digitalWrite(OUTPUT_01, LOW);
  }
  
  val_02 = digitalRead(INPUT_02);
  if(val_02 == HIGH){
    digitalWrite(OUTPUT_02, HIGH);
  }else{
    digitalWrite(OUTPUT_02, LOW);
  }
  
  val_03 = digitalRead(INPUT_03);
  if(val_03 == HIGH){
    digitalWrite(OUTPUT_03, HIGH);
  }else{
    digitalWrite(OUTPUT_03, LOW);
  }
  
  val_04 = digitalRead(INPUT_04);
  if(val_04 == HIGH){
    digitalWrite(OUTPUT_04, HIGH);
  }else{
    digitalWrite(OUTPUT_04, LOW);
  }
  
  val_05 = digitalRead(INPUT_05);
  if(val_05 == HIGH){
    digitalWrite(OUTPUT_05, HIGH);
  }else{
    digitalWrite(OUTPUT_05, LOW);
  }
}
