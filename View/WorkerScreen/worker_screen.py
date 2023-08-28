from View.base_screen import BaseScreenView
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen


class MobileSView(MDScreen):
    pass



class TabletSView(MDScreen):
    pass



class DesktopSView(MDScreen):
    pass


class WorkerScreenView(MDResponsiveLayout,BaseScreenView):

    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileSView()
        self.tablet_view = TabletSView()
        self.desktop_view = DesktopSView()

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    

