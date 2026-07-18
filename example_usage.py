from client import SpeaklyMeetingTranslatorClient
client = SpeaklyMeetingTranslatorClient()
transcript = [
    {"speaker": "Alice", "text": "Let us review the Q3 targets.", "lang": "en"},
    {"speaker": "Hiroshi", "text": "Q3の目標を確認しましょう。", "lang": "ja"},
    {"speaker": "Maria", "text": "Revisemos los objetivos del Q3.", "lang": "es"}
]
result = client.normalize_transcript(transcript)
print(f"Meeting notes ({result['speaker_count']} speakers):")
print(result["unified_notes"])
