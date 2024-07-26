import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE

    header = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    padding=40,
                    content=ft.Image(src='pedro.png'),
                    shape=ft.BoxShape.CIRCLE,
                    height=200,
                ),
                ft.Container(
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text(
                                        value='Pedro de Castro Kurtz',
                                        color=ft.colors.BLACK,
                                        size=24,
                                    ),
                                    ft.Icon(
                                        name=ft.icons.VERIFIED,
                                        color=ft.colors.BLUE_500,
                                        size=20,
                                    )
                                ]
                            ),

                            ft.Icon(
                                name=ft.icons.MORE_HORIZ,
                                color=ft.colors.BLACK
                            )
                        ]
                    )
                )
            ]
        )
    )

    layout = ft.Container(
        width = 900,
        content=ft.Column(
            controls=[
                header,

            ]
        )
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')