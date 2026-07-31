from nicegui import ui
from chat_link import handle_send

# -------------------------------------------------------------------------
# THEME CONFIGURATION & PALETTE
# -------------------------------------------------------------------------
ui.colors(
    primary='#697565',
    secondary='#3C3D37',
    accent='#ECDFCC',
    dark='#1E201E',
    dark_page='#1E201E'
)

ui.add_css('''
    /* Dark Mode Text Adjustments */
    body.body--dark { background-color: #1E201E; color: #ECDFCC; }
    body.body--dark .q-message-text { background-color: #3C3D37 !important; color: #ECDFCC !important; }
    body.body--dark .q-message-text--sent { background-color: #697565 !important; color: #ECDFCC !important; }

    /* Light Mode Text Adjustments */
    body:not(.body--dark) { background-color: #ECDFCC; color: #1E201E; }
    body:not(.body--dark) .q-message-text { background-color: #FFFFFF !important; color: #1E201E !important; }
    body:not(.body--dark) .q-message-text--sent { background-color: #697565 !important; color: #FFFFFF !important; }
''')

dark_mode = ui.dark_mode()
dark_mode.enable()

# -------------------------------------------------------------------------
# LAYOUT & UI COMPONENTS
# -------------------------------------------------------------------------

# Header with Theme Toggle Switch
with ui.header().classes('bg-[#3C3D37] text-[#ECDFCC] px-6 py-3 flex justify-between items-center'):
    ui.label('Chuchu AI Interface').style('font-size: 20px; font-weight: bold;')
    ui.switch('Dark Mode', value=True, on_change=lambda e: dark_mode.value if e.value else dark_mode.disable()).props('color=primary')

# Main Scrolling Chat Container
with ui.column().classes('w-full max-w-3xl mx-auto p-4 q-pa-md flex-grow mb-20'):
    chat_container = ui.column().classes('w-full items-stretch')

# Fixed Bottom Footer Input Bar
with ui.footer().classes('bg-[#1E201E] p-4 border-t border-[#3C3D37]'):
    with ui.row().classes('w-full max-w-3xl mx-auto no-wrap items-center'):
        chat_input = ui.input(placeholder='Message the AI...').props('rounded outlined dark dense input-class=mx-3').classes('w-full self-center bg-[#3C3D37] text-[#ECDFCC] rounded-full')

        # Bind the Enter key and Send button to our clean logic file
        chat_input.on('keydown.enter', lambda: handle_send(chat_input, chat_container))
        ui.button('Send', on_click=lambda: handle_send(chat_input, chat_container), color='primary').props('rounded')
ui.run(title="Custom AI Chat")
