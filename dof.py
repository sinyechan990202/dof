import time
import Adafruit_PCA9685

# Adafruit_PCA9685 라이브러리를 사용하여 PCA9685 모듈을 초기화합니다.
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

# 각 관절을 제어하기 위한 채널 번호를 정의합니다.
SERVO1_CHANNEL = 0
SERVO2_CHANNEL = 1
SERVO3_CHANNEL = 2
SERVO4_CHANNEL = 3
SERVO5_CHANNEL = 4
SERVO6_CHANNEL = 5

# 서보 모터 제어 함수를 정의합니다.
def set_servo(channel, angle):
    pulse = int(4096 * ((angle * 11) + 500) / 20000)
    pwm.set_pwm(channel, 0, pulse)

# 로봇 팔을 초기 위치로 설정합니다.
set_servo(SERVO1_CHANNEL, 90)
set_servo(SERVO2_CHANNEL, 90)
set_servo(SERVO3_CHANNEL, 90)
set_servo(SERVO4_CHANNEL, 90)
set_servo(SERVO5_CHANNEL, 90)
set_servo(SERVO6_CHANNEL, 90)

# 로봇 팔을 이동시키는 함수를 정의합니다.
def move_arm(servo1_angle, servo2_angle, servo3_angle, servo4_angle, servo5_angle, servo6_angle):
    set_servo(SERVO1_CHANNEL, servo1_angle)
    set_servo(SERVO2_CHANNEL, servo2_angle)
    set_servo(SERVO3_CHANNEL, servo3_angle)
    set_servo(SERVO4_CHANNEL, servo4_angle)
    set_servo(SERVO5_CHANNEL, servo5_angle)
    set_servo(SERVO6_CHANNEL, servo6_angle)
    time.sleep(0.5)

# 로봇 팔을 동작시키는 코드입니다.
move_arm(45, 90, 90, 45, 90, 90)
move_arm(135, 90, 90, 135, 90, 90)
move_arm(90, 45, 90, 90, 45, 90)
move_arm(90, 135, 90, 90, 135, 90)
move_arm(90, 90, 45, 90, 90, 45)
move_arm(90, 90, 135, 90, 90, 135)
