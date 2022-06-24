from controller.controllerMotorista import ControllerMotorista
from model.google import API, Google
from view.viewRota import ViewRota


if __name__ == "__main__":
    var = API.request(
        f'Rua Lauro Linhares, Florianópolis, Santa Catarina, Brasil')
    print(var.rows)
