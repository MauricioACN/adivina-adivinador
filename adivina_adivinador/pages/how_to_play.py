import reflex as rx
from adivina_adivinador.routes import Route
import adivina_adivinador.utils as utils
from adivina_adivinador.styles.styles import Size, Spacing
from adivina_adivinador.styles.colors import Color, TextColor
import adivina_adivinador.styles.styles as styles
from adivina_adivinador.components.navbar import navbar


@rx.page(
    route=Route.HOW_TO_PLAY.value,
    title=utils.how_to_play_title,
    description=utils.how_to_play_description,
    image=utils.preview,
    meta=utils.how_to_play_meta
)
def how_to_play() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.box(
            rx.section(
                rx.heading("Como jugar?",
                           color=Color.PRIMARY.value),
                rx.divider(size="4"),
                rx.text("¡Bienvenido al juego Adivina Adivinador! Aquí te explicamos cómo funciona:",
                        color=TextColor.BODY.value),
                rx.list.ordered(
                    rx.list.item(
                        "En la pantalla aparecerá una palabra (Objetos: Cuchillo, Silla, Mesa, etc.)"),
                    rx.list.item(
                        "Tu tarea es dar pistas para que la persona que está frente a ti pueda adivinar esa palabra."),
                    rx.list.item(
                        "Intenta dar pistas que no sean tan obvias, pero tampoco tan difíciles. Tip: usa situaciones donde se use el objeto."),
                    rx.list.item(
                        "Si la persona adivina correctamente, Verás una instrucción indicando hacia qué lado debes pasar el celular."),
                    rx.list.item(
                        "Si no adivinan la palabra, simplemente toca la pantalla para cambiarla. Una nueva palabra aparecerá y deberás dar nuevas pistas para que adivine."),
                    rx.list.item(
                        "Pero, ¡cuidado! Si tienes el celular cuando el tiempo se acabe, ¡pierdes!"),
                    color=TextColor.BODY.value,
                    margin_bottom=Size.MEDIUM.value
                ),
                rx.divider(size="4"),
                rx.text("Ejemplo:", color=TextColor.BODY.value),
                rx.list.unordered(
                    rx.list.item("Palabra: Cuchillo"),
                    rx.list.item(
                        "Pistas: Se usa para cortar | es de metal | se usa en la cocina."),
                    color=TextColor.BODY.value,
                ),
                margin_y=Size.LARGE.value,
                padding=Size.LARGE.value,
            )

        ),
        rx.flex(
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
        ),
        # footer()
    )
