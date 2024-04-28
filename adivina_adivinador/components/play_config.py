import reflex as rx
# import asyncio
import adivina_adivinador.constants as constants


class PlayConfigPanel(rx.State):
    players: str = constants.default_players
    category: str = constants.default_category

    def set_players(self, value: str):
        self.players = value

    def set_category(self, value: str):
        self.category = value


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
                                "Parametro"
                            ),
                            rx.table.column_header_cell(
                                "Valor"
                            ),
                        ),
                    ),
                    rx.table.body(
                        rx.table.row(
                            rx.table.row_header_cell(
                                "Cantidad de Jugadores"
                            ),
                            rx.table.cell(
                                rx.select(
                                    constants.PLAYERS,
                                    default_value=constants.default_players,
                                    on_change=PlayConfigPanel.set_players
                                )
                            ),
                        ),
                        rx.table.row(
                            rx.table.row_header_cell(
                                "Categoria"
                            ),
                            rx.table.cell(
                                rx.select(
                                    constants.CATEGORIES,
                                    default_value=constants.default_category,
                                    on_change=PlayConfigPanel.set_category
                                )
                            ),
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
                        "Cerrar",
                        variant="soft",
                        color_scheme="gray",
                    ),
                ),
                spacing="3",
                justify="end",
            )
        ),
    )
