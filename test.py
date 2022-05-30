from controller.controllerMotorista import ControllerMotorista

if __name__ == "__main__":
    while True:
        value = ControllerMotorista().options()
        if value == 'Exit':
            break
