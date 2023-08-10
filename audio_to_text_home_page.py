import streamlit as st
from streamlit_option_menu import option_menu
import openai


def auido_to_text(audio):
    openai.api_key = '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'
    result = openai.Audio.transcribe("whisper-1", audio, verbose=True)
    return result


def video_to_text(video):
    openai.api_key = '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'
    result = openai.Audio.transcribe("whisper-1", video, verbose=True)
    return result


selected = option_menu(
    menu_title=None,
    options=['Intro', 'Audio', 'Video'],
    icons=['menu-app', 'music-note', 'file-earmark-play'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal'
)
if selected == 'Intro':
    st.write("Intro of the application")
elif selected == 'Audio':
    audio = st.file_uploader("Upload an audio file", type=["mp3"])
    if audio is not None:
        with st.spinner("Converting audio to speech...."):
            result = auido_to_text(audio)
        with st.container():
            st.write(result['text'])
elif selected == 'Video':
    video = st.file_uploader("Upload video file", type=['mp4'])
    if video is not None:
        with st.spinner("Converting video to speech...."):
            result = video_to_text(video)
        with st.container():
            st.write(result['text'])
