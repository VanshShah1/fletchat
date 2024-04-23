import flet as ft

def main(page: ft.Page):
    page.title = "𝕏"
    page.bgcolor="black"
    
    title=ft.Container(ft.Text("𝕏",
                  color="white",
                  size=50,
                ),
                padding=50)
    tweetblock=ft.Container(
        ft.Row([ft.CircleAvatar(), ft.Column([ft.Text('helo wold', size=20), ft.IconButton(icon=ft.icons.THUMB_UP_ROUNDED)])]),
        padding=10,
        border=ft.border.all(1, ft.colors.GREY_900),
        border_radius=10,
        width=800,
        margin=ft.margin.Margin(left=300, right=300, top=0, bottom=10)
    )
    tweets=ft.Container(
        ft.Column(
            controls=[tweetblock, tweetblock]
        )
    )
    page.add(title,
            tweets)

ft.app(main)