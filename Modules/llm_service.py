import os
from google import genai

client = genai.Client()

async def stream_ai_response(prompt: str):
    """
    Sends a prompt to the Gemini API and yields the response asynchronously.
    """
    try:
        # ADD 'await' right here before client.aio...
        response_stream = await client.aio.models.generate_content_stream(
            model="gemini-3.6-flash",
            contents=prompt
        )

        async for chunk in response_stream:
            if chunk.text:
                yield chunk.text

    except Exception as e:
        yield f"\n\n**Error:** {str(e)}"
