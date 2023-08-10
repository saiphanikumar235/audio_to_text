import openai


def auido_to_text(audio):
    openai.api_key = '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'
    result = openai.Audio.transcribe("whisper-1", audio, verbose=True)
    return result


def video_to_text(audio):
    openai.api_key = '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'
    result = openai.Audio.transcribe("whisper-1", audio, verbose=True)
    return result