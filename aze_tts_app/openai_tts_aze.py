 # onyx, shimmer and nova are the best one.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pathlib import Path
from openai import OpenAI 

@api_view(['POST'])
def generate_audio(request):
    text= request.data.get("text", '')
    voice = request.data.get("voice", 'onyx')
    
    client = OpenAI(api_key= "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")

    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
      model="tts-1",
      voice=voice, 
      input= text
    )

    response.stream_to_file(speech_file_path)

    return Response({'message': "Audio generated successfully"})