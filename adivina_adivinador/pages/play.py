import reflex as rx
from adivina_adivinador.routes import Route
import adivina_adivinador.utils as utils
from adivina_adivinador.components.navbar import navbar
from adivina_adivinador.styles.styles import Spacing, Size
from adivina_adivinador.components.play_config import play_config_panel, PlayConfigPanel
import asyncio


class MyTaskState(rx.State):
    counter: int = 10
    running: bool = False
    _n_tasks: int = 0

    @rx.background
    async def my_task(self):
        async with self:
            # The latest state values are always available inside the context
            if self._n_tasks > 0:
                # only allow 1 concurrent task
                return

            # State mutation is only allowed inside context block
            self._n_tasks += 1

        while True:
            async with self:
                if self.counter <= 0:
                    self.clear_counter()
                if not self.running:
                    self._n_tasks -= 1
                    return
                self.counter -= 1

            # Await long operations outside the context to avoid blocking UI
            await asyncio.sleep(0.5)

    def toggle_running(self):
        self.running = not self.running
        if self.running:
            return MyTaskState.my_task

    def clear_counter(self):
        self.counter = 10
        self.running = False


def timer_example():
    return rx.flex(
        rx.button(
            rx.cond(~MyTaskState.running, "Jugar", "Detener"),
            on_click=MyTaskState.toggle_running,
            size="4"
        ),
        # rx.button(
        #     "Reiniciar",
        #     on_click=MyTaskState.clear_counter,
        #     size="4"
        # ),
        spacing=Spacing.SMALL.value,
        # direction="column",
        widht="100%",
        max_width="100%"
    )


@rx.page(
    route=Route.PLAY.value,
    title=utils.play_title,
    description=utils.play_description,
    image=utils.preview,
    meta=utils.play_meta
)
def play() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.flex(
            play_config_panel(),
            timer_example(),
            # direction="row",
            spacing=Spacing.SMALL.value,
            # max_width="100%",
            width="100%",
            margin_y=Size.LARGE.value,
            padding=Size.LARGE.value
        ),
        rx.heading(MyTaskState.counter, size="8"),
        rx.divider(size="4"),
        rx.text(PlayConfigPanel.players, size="2"),
        rx.text(PlayConfigPanel.category, size="2"),
    )
