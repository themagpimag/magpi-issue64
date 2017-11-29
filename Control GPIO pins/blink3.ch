#!/bin/ch
/* File: blink3.ch*/

gpio -g mode 4 out
while(1) {
  gpio -g write 4 1
  delay(500);
  gpio -g write 4 0
  delay(500);
}
