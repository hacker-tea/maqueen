def on_forever():
    maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 255)
    maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 255)
    basic.pause(1000)
    maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 255)
    maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 0)
    basic.pause(1000)
    maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 0)
    maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 255)
    basic.pause(1000)
    maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CCW, 255)
    maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CCW, 255)
    basic.pause(1000)
    maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CCW, 255)
    maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CCW, 0)
    basic.pause(1000)
basic.forever(on_forever)
