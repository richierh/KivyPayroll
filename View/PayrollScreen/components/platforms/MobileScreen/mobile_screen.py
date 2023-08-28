from kivymd.uix.screen import MDScreen


class MobileScreenView(MDScreen):
    
    
    def worker_page(self):

        self.parent.manager_screens.current='worker screen'
        pass