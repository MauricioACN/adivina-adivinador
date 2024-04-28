import reflex as rx
# import asyncio


class CountState(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


# class TimerState(rx.State):
#     count: int = 120  # Starting value for the countdown
#     running: bool = False  # Estado para gestionar si el contador está activo

#     async def countdown(self):
#         if not self.running:  # Solo inicia si no está ya corriendo
#             self.running = True

#         while self.count > 0 and self.running:
#             await asyncio.sleep(1)  # Espera 1 segundo
#             self.count -= 1  # Decrementa el contador
#             yield  # Actualiza la UI
#         self.running = False

#     def reset_timer(self):
#         self.running = False


def counter():
    return rx.flex(
        rx.button(
            "Disminuir",
            color_scheme="red",
            on_click=CountState.decrement,
        ),
        rx.heading(CountState.count),
        rx.button(
            "Aumentar",
            color_scheme="grass",
            on_click=CountState.increment,
        ),
        spacing="3",
    )


# def timer_example():
#     return rx.cond(
#         TimerState.running,
#         rx.button("Reiniciar", on_click=TimerState.reset_timer, size="4"),
#         rx.button("Jugar", on_click=TimerState.countdown, size="4")
#     )


def play_config_panel() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon("cog"), size="4")),
        rx.dialog.content(
            rx.dialog.title("Configuración de la Partida"),
            rx.dialog.description(
                "Configure la partida con los siguientes ajustes:"
            ),
            rx.inset(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell(
                                "Full Name"
                            ),
                            rx.table.column_header_cell(
                                "Email"
                            ),
                            rx.table.column_header_cell(
                                "Group"
                            ),
                        ),
                    ),
                    rx.table.body(
                        rx.table.row(
                            rx.table.row_header_cell(
                                "Danilo Rosa"
                            ),
                            rx.table.cell("danilo@example.com"),
                            rx.table.cell("Developer"),
                        ),
                        rx.table.row(
                            rx.table.row_header_cell(
                                "Zahra Ambessa"
                            ),
                            rx.table.cell("zahra@example.com"),
                            rx.table.cell("Admin"),
                        ),
                    ),
                ),
                side="x",
                margin_top="24px",
                margin_bottom="24px",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Close",
                        variant="soft",
                        color_scheme="gray",
                    ),
                ),
                spacing="3",
                justify="end",
            ),
        ),
    )
