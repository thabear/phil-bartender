int INPUT_00 = 0;
int INPUT_01 = 1;
int INPUT_02 = 2;
int INPUT_03 = 3;
int INPUT_04 = 4;
int INPUT_05 = 5;

int OUPUT_00 = 14;
int OUPUT_01 = 15;
int OUPUT_02 = 16;
int OUPUT_03 = 17;
int OUPUT_04 = 18;
int OUPUT_05 = 19;

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
  
  pinmode(OUTPUT_00, OUTPUT);
  pinmode(OUTPUT_01, OUTPUT);
  pinmode(OUTPUT_02, OUTPUT);
  pinmode(OUTPUT_03, OUTPUT);
  pinmode(OUTPUT_04, OUTPUT);
  pinmode(OUTPUT_05, OUTPUT);
}

void loop()
{
  val_00 = digitalRead(INPUT_00);
  digitalWrite(OUTPUT_00, val_00);
  
  val_01 = digitalRead(INPUT_01);
  digitalWrite(OUTPUT_01, val_01);
  
  val_02 = digitalRead(INPUT_02);
  digitalWrite(OUTPUT_02, val_02);
  
  val_03 = digitalRead(INPUT_03);
  digitalWrite(OUTPUT_03, val_03);
  
  val_04 = digitalRead(INPUT_04);
  digitalWrite(OUTPUT_04, val_04);
  
  val_05 = digitalRead(INPUT_05);
  digitalWrite(OUTPUT_05, val_05);
}
