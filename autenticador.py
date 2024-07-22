import flet as ft

def main(page:ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True
    page.windows_resizable = False

    def logar(e):
        page.remove(register)
        page.add(login)
        page.update()

    def registrar(e):
        page.remove(login)
        page.add(register)
        page.update()

    login = ft.Column([
        ft.Container(
            bgcolor=ft.colors.GREEN_200,
            width=page.window_width - 100,
            height=page.window_height - 60,
            border_radius=10,

            content=ft.Column([
                ft.Container(
                    bgcolor=ft.colors.WHITE70,
                    width=400,
                    height=320,
                    border_radius=10,

                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(
                                top=10,
                                bottom=12
                            ),
                            
                            content = ft.Column([
                                ft.Text(
                                    value='Login',
                                    weight='bold',
                                    size=20
                                )
                            ])
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text='Email',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.EMAIL
                            ),

                            ft.TextField(
                                hint_text='Senha',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                            ),

                            ft.ElevatedButton(
                                text='Login',
                                bgcolor=ft.colors.GREEN_200,
                                on_hover=ft.colors.GREEN_200,
                                width=300,
                                height=40
                            ),

                            ft.Row([
                                ft.TextButton('Recuperar conta'),
                                ft.TextButton(
                                    text='Cria nova conta',
                                    on_click= registrar
                                    )
                            ],width=300,alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

                        ],spacing=8),

                        ft.Row([
                            ft.IconButton(icon=ft.icons.EMAIL),
                            ft.IconButton(icon=ft.icons.FACEBOOK),
                            ft.IconButton(icon=ft.icons.TELEGRAM)
                        ],alignment='center')
                    ],horizontal_alignment='center')
                )
            ],horizontal_alignment='center', alignment='center')
        )
    ])

    register = ft.Column([
        ft.Container(
            bgcolor=ft.colors.GREEN_200,
            width=page.window_width - 100,
            height=page.window_height - 60,
            border_radius=10,

            content=ft.Column([
                ft.Container(
                    bgcolor=ft.colors.WHITE70,
                    width=400,
                    height=450,
                    border_radius=10,

                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(
                                top=10,
                                bottom=12
                            ),
                            
                            content = ft.Column([
                                ft.Text(
                                    value='Register',
                                    weight='bold',
                                    size=20
                                )
                            ])
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text='Nome',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.NAME
                            ),
                            
                            ft.TextField(
                                hint_text='Sobrenome',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.NAME
                            ),

                            ft.TextField(
                                hint_text='Senha',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                            ),

                            ft.TextField(
                                hint_text='Confirmar Senha',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD
                            ),

                            ft.TextField(
                                hint_text='Email',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.EMAIL,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.EMAIL
                            ),

                            ft.TextField(
                                hint_text='Telefone',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PHONE,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.PHONE
                            ),

                            ft.ElevatedButton(
                                text='Register',
                                bgcolor=ft.colors.GREEN_200,
                                on_hover=ft.colors.GREEN_200,
                                width=300,
                                height=40
                            ),

                            ft.Row([
                                ft.TextButton('Recuperar conta'),
                                ft.TextButton(
                                    text='Fazer Login',
                                    on_click= logar
                                    )
                            ],width=300,alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

                        ],spacing=8),

                        
                    ],horizontal_alignment='center')
                )
            ],horizontal_alignment='center', alignment='center')
        )
    ])


    page.add(register)
if __name__ == '__main__':
    ft.app(target=main)