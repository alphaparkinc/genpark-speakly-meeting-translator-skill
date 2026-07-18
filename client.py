class SpeaklyMeetingTranslatorClient:
    def normalize_transcript(self, multilingual_transcript: list) -> dict:
        speakers = set()
        lines = []
        for entry in multilingual_transcript:
            speaker = entry.get("speaker", "Unknown")
            text = entry.get("text", "")
            lang = entry.get("lang", "en")
            speakers.add(speaker)
            # Mock translation marker
            note = f"[{speaker}]: {text}" if lang == "en" else f"[{speaker}] (translated from {lang}): {text}"
            lines.append(note)
        return {"unified_notes": "\n".join(lines), "speaker_count": len(speakers)}
