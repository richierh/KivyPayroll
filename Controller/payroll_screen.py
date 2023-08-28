import importlib

import View.PayrollScreen.payroll_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.PayrollScreen.payroll_screen)




class PayrollScreenController:
    """
    The `PayrollScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.payroll_screen.PayrollScreenModel
        self.view = View.PayrollScreen.payroll_screen.PayrollScreenView(controller=self, model=self.model)

    def get_view(self) -> View.PayrollScreen.payroll_screen:
        return self.view
