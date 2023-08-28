# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.payroll_screen import PayrollScreenModel
from Controller.payroll_screen import PayrollScreenController
from Model.worker_screen import WorkerScreenModel
from Controller.worker_screen import WorkerScreenController
from Model.worker_screen import WorkerScreenModel
from Controller.worker_screen import WorkerScreenController
from Model.worker_screen import WorkerScreenModel
from Controller.worker_screen import WorkerScreenController
from Model.worker_screen import WorkerScreenModel
from Controller.worker_screen import WorkerScreenController

screens = {
    'payroll screen': {
        'model': PayrollScreenModel,
        'controller': PayrollScreenController,
    },
    'worker screen': {
        'model': WorkerScreenModel,
        'controller': WorkerScreenController,
    },
    'main screen': {
        'model': MainScreenModel,
        'controller': MainScreenController,
    },
}