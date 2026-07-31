from nicegui import ui
from llm_service import stream_ai_response

async def handle_send(chat_input, chat_container) -> None:
    """
    Handles the user input, updates the UI chat container,
    and streams responses from the AI model.
    """
    question = chat_input.value
    if not question.strip():
        return

    chat_input.value = ''

    try:
        with chat_container:
            # 1. User Message Box
            ui.chat_message(text=question, name='You', sent=True)

            # 2. AI Message Box & Loading Spinner
            response_message = ui.chat_message(name='AI', sent=False)
            spinner = ui.spinner(type='dots', color='primary')

            response_text = ""
            async for chunk in stream_ai_response(question):
                response_text += chunk
                response_message.clear()
                with response_message:
                    ui.markdown(response_text)
                ui.run_javascript('window.scrollTo(0, document.body.scrollHeight)')

            chat_container.remove(spinner)

    except Exception as e:
        ui.notify(f"Error: {e}", type='negative')
