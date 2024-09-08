import flet as ft


class Alert:
    def __init__(self, page):
        self.page = page
        #self.dlg
        #self.dlg_modal
   
    def alert(self, msg):
        dlg = ft.AlertDialog(
            title=ft.Text(msg),
            #on_dismiss=lambda e: self.page.add(ft.Text("Non-modal dialog dismissed")),
        )

        def handle_close(e):
            self.page.close(self.dlg_modal)
            self.page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes", on_click=handle_close),
                ft.TextButton("No", on_click=handle_close),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: self.page.add(
                ft.Text("Modal dialog dismissed"),
            ),
        )

        self.page.open(dlg)
    '''page.add(
        ft.ElevatedButton("Open dialog", on_click=lambda e: page.open(dlg)),
        ft.ElevatedButton("Open modal dialog", on_click=lambda e: page.open(dlg_modal)),
    )'''


