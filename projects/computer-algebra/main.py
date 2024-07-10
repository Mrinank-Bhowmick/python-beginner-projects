from newton_command import NEWTON_CMDS_DICT

import dearpygui.dearpygui as dpg


def selection_cb(sender, app_data, user_data):
    """Callback function for button selections in the message box."""
    if user_data[1]:
        print("User selected 'Ok'")
    else:
        print("User selected 'Cancel'")

    # delete window
    dpg.delete_item(user_data[0])


def show_info(title, message, selection_callback):
    """
    Display an information message box with title, message, and callback.

    References:
        https://github.com/hoffstadt/DearPyGui/discussions/1002
    """

    # guarantee these commands happen in the same frame
    with dpg.mutex():
        viewport_width = dpg.get_viewport_client_width()
        viewport_height = dpg.get_viewport_client_height()

        with dpg.window(
            tag="popup-window", label=title, modal=True, no_close=True
        ) as modal_id:
            dpg.add_text(message)
            dpg.add_button(
                label="Ok",
                width=75,
                user_data=(modal_id, True),
                callback=selection_callback,
            )
            dpg.add_same_line()
            dpg.add_button(
                label="Cancel",
                width=75,
                user_data=(modal_id, False),
                callback=selection_callback,
            )

    # guarantee these commands happen in another frame
    dpg.split_frame()
    width = dpg.get_item_width(modal_id)
    height = dpg.get_item_height(modal_id)
    dpg.set_item_pos(
        modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2]
    )


# Callbacks and Helpers
def on_evaluate(sender, app_data, user_data):
    """Callback function for the 'Evaluate' button."""
    # Get the Command
    cmd = dpg.get_value("radio-cmds")
    cmd_func = NEWTON_CMDS_DICT[cmd]

    # Get the Expression
    expr = dpg.get_value("inp-expr")

    if expr.strip() in [""]:
        show_info("Error", "Please use valid mathematical expressions.", selection_cb)
        # Clear Expression
        dpg.set_value("inp-expr", "")
        return

    # Evaluate
    response = cmd_func(expr)
    result = response.result

    dpg.set_value("label-output", result)


dpg.create_context()
dpg.create_viewport(title="Computer Algebra", width=1300, height=750)

with dpg.window(
    tag="inp-window",
    label="Input",
    pos=[0, 0],
    autosize=True,
    # width=1150,
    # height=350,
    no_collapse=True,
    no_close=True,
):
    # Radio Button for Commands
    dpg.add_radio_button(
        horizontal=True,
        tag="radio-cmds",
        items=[cmd for cmd in NEWTON_CMDS_DICT.keys()],
    )

    # Text Area for Mathematical Expression
    dpg.add_input_text(
        tag="inp-expr",
        width=int(1150 * 0.8),
    )

    # Button for Evaluating Command and Expression
    dpg.add_button(label="Evaluate", callback=on_evaluate)

with dpg.window(
    tag="out-window",
    pos=[0, 100],
    label="Output",
    # width=700,
    # height=350,
    autosize=True,
    no_collapse=True,
    no_close=True,
):
    # Use Label for Output
    dpg.add_text(
        tag="label-output",
        label="Result",
        show_label=True,
    )

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
