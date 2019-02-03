void setup() {
  // put your setup code here, to run once:
  pinMode(3, OUTPUT);
  Serial.begin(9600);
  analogWrite(3, 127);
}

char buffer[16];
int pos;

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    char c = Serial.read();
    if (c == '\n' || c == '\r') {
      buffer[pos] = '\0';
      int val = atoi(buffer);
      if (val >=0 && val <=255) {
        analogWrite(3, val);
        Serial.print("set ");
        Serial.println(val);
      }
      pos = 0;
    } else {
      if (pos >=15) {
        pos = 0;
      }
      buffer[pos] = c;
      pos++;
    }
  }
}
