from controller.controllerMotorista import ControllerMotorista
from dao.daoPercuso import DaoPercurso
from dao.daoPonto import DaoPonto
from dao.daoRota import DaoRota
from model.google import API, Google
from model.percurso import Percurso
from model.rota import Rota
from view.viewRota import ViewRota

spots = DaoPonto.list()
route = Rota(tempo_estimado=10)
DaoRota.insert(route)

for cur, nxt in zip(spots, spots[1:] + ['end']):
    if nxt == 'end':
        break
    else:
        road = Percurso(pontoA=cur, pontoB=nxt, rota=route)
        DaoPercurso.insert(road)
