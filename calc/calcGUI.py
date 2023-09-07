import flet as ft

# data = [
#     ["AC","%","del","÷"],
#     ["7","8","9","x"],
#     ["4","5","6","-"],
#     ["1","2","3","+"],
#     ["0",".","="]
# ]

def main(page: ft.Page):
    page.theme_mode = "dark"
    page.vertical_alignment = "end"
    page.padding = 0
    text = ft.Ref[ft.TextField]()

    def press(e:ft.ControlEvent):
        data = e.control.data
        if data in ("1","2","3","4","5","6","7","8","9","0",".","+","x","÷","-","%"):
            text.current.value+=data
        elif data == "del":
            text.current.value = text.current.value[:-1]
        else:
            text.current.value = ''
        text.current.error_text = ""
        page.update()
    
    def equal(e):
        try:
            text.current.value = str(eval(str(text.current.value).replace("x","*").replace("÷","/").replace("%","/100")))
        except:
            text.current.error_text = "SyntaxError"
        page.update()
    
    col = ft.Container(
        bgcolor=ft.colors.BLACK45,
        padding=20,
        border_radius=ft.border_radius.only(20,20),
        content=ft.Column(
                spacing=20,
                controls=[
                    ft.Row(
                        [
                            ft.TextField(ref=text,expand=1,text_size=20,keyboard_type="none")
                        ]
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                                text="AC",
                                                expand=1,
                                                data="AC",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="%",
                                                expand=1,
                                                data="%",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="del",
                                                expand=1,
                                                data="del",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="÷",
                                                expand=1,
                                                data="÷",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20)
                                        )
                        ]
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                                text="7",
                                                expand=1,
                                                data="7",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="8",
                                                expand=1,
                                                data="8",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="9",
                                                expand=1,
                                                data="9",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="x",
                                                expand=1,
                                                data="x",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20)
                                        )
                        ]
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                                text="4",
                                                expand=1,
                                                data="4",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="5",
                                                expand=1,
                                                data="5",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="6",
                                                expand=1,
                                                data="6",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="-",
                                                expand=1,
                                                data="-",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20)
                                        )
                        ]
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                                text="1",
                                                expand=1,
                                                data="1",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="2",
                                                expand=1,
                                                data="2",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="3",
                                                expand=1,
                                                data="3",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="+",
                                                expand=1,
                                                data="+",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20)
                                        )
                        ]
                    ),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                                text="0",
                                                expand=2,
                                                data="0",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text=".",
                                                expand=1,
                                                data=".",
                                                on_click = press,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20,shadow_color=ft.colors.TRANSPARENT,bgcolor=ft.colors.TRANSPARENT,surface_tint_color=ft.colors.TRANSPARENT)
                                        ),
                            ft.ElevatedButton(
                                                text="=",
                                                expand=1,
                                                data="=",
                                                on_click = equal,
                                                scale=1.2,
                                                style=ft.ButtonStyle(shape=ft.CircleBorder(),padding=20)
                                        )
                        ]
                    )
                ]
        )
    )
    
    page.add(col)
ft.app(target=main)