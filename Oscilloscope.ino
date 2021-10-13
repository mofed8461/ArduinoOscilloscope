void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}
#define ARR_SIZE 1024
float arr[ARR_SIZE];
int counter = 0;
void loop() {
  float next = (analogRead(0) / 1024.0) * 5.0;
  if (counter != 0) {
//    if (abs(arr[counter - 1] - next) > 0.0001)
      arr[counter++] = next;
  }
  else {
    arr[counter++] = next;
  }
  
  if (counter >= ARR_SIZE) {
    counter = 0;
    for (int i = 0; i < ARR_SIZE; ++i)
      Serial.println(String(arr[i]));
  }
}
