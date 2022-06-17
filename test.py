from controller.controllerMotorista import ControllerMotorista
from view.viewRota import ViewRota

numbers = ['Rota 01', 'Rota 02', 'Rota 03', 'Rota 04']


if __name__ == "__main__":
    while True:
        value = ViewRota().options(numbers)
