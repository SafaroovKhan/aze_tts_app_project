from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from openai import OpenAI
from django.http import JsonResponse
from urllib.parse import urlparse
from pathlib import Path

@api_view(['POST'])
def generate_audio(request):
    text = request.data.get("text", '')
    voice = request.data.get("voice", 'onyx')

    client = OpenAI(api_key="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")

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=text
    )

    response.stream_to_file(speech_file_path)

    audio_file_url = f"{settings.MEDIA_URL}speech.mp3"

    return JsonResponse({
        'message': "Audio generated successfully",
        'audio_file_url': audio_file_url,
    })
