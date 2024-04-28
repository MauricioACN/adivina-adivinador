import reflex as rx
from adivina_adivinador.styles.styles import Spacing, Size
import adivina_adivinador.utils as utils
from adivina_adivinador.components.navbar import navbar
from adivina_adivinador.routes import Route


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.flex(
            rx.card(
                rx.link(
                    rx.heading("Aprende a Jugar", align="center"), href=Route.HOW_TO_PLAY.value
                ), size='4'
            ),
            rx.card(
                rx.link(
                    rx.heading("Jugar", align="center"), href=Route.PLAY.value
                ), size='4'
            ),
            direction="column",
            spacing=Spacing.LARGE.value,
            max_width="100%",
            width="100%",
            margin_y=Size.LARGE.value,
            padding=Size.LARGE.value
        )
    )
