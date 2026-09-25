import asyncio
import streamlit as st

from copilot import CopilotClient
from prompts import SYSTEM_PROMPT


st.set_page_config(
    page_title="Career Mentor Agent",
    page_icon="🤖"
)

st.title("🤖 Career Mentor Agent")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


async def get_career_advice(messages):

    client = CopilotClient()

    await client.start()

    try:
        session = await client.create_session(
            model="gpt-5.4"
        )

        conversation = SYSTEM_PROMPT + "\n\n"

        for message in messages:
            conversation += (
                f"{message['role'].upper()}: "
                f"{message['content']}\n\n"
            )

        response = await session.send_and_wait(
            conversation
        )

        return response.data.content

    finally:
        await client.stop()


prompt = st.chat_input(
    "Ask me about careers..."
)


if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                answer = asyncio.run(
                    get_career_advice(
                        st.session_state.messages
                    )
                )

                st.write(answer)

            except Exception as e:

                answer = f"Error: {str(e)}"

                st.error(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
