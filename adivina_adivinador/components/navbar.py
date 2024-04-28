import reflex as rx
from adivina_adivinador.routes import Route
from adivina_adivinador.styles.styles import Size
from adivina_adivinador.styles.colors import Color
import adivina_adivinador.styles.styles as styles


def resources_item(text, url, icon):
    return rx.link(
        rx.flex(
            rx.icon(icon, size=20, color=rx.color("mauve", 9)),
            rx.text(text, color=rx.color("mauve", 9)),
            wrap="nowrap",
            spacing="2",
        ),
        href=url,
    )


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("Adivina Adivinador",
                        color=Color.PRIMARY.value,
                        style=styles.navbar_title_style),
            ),
            href=Route.INDEX.value
        ),
        rx.spacer(),
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    rx.icon("menu", size=20))
            ),
            rx.menu.content(
                rx.menu.item(
                    rx.link("Como Jugar", href=Route.HOW_TO_PLAY.value, hover=Color.SECONDARY.value)),
                rx.menu.item("Contacto", href=Route.CONTACT.value),
                rx.menu.item("Feedback", href=Route.FEEDBACK.value)
            )
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )
