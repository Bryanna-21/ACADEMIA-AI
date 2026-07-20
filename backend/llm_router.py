import random
import httpx
from dotenv import load_dotenv
import os

load_dotenv()

class LLMRouter:
    def __init__(self):
        self.providers = {
            "grok": os.getenv("GROK_API_KEYS", "").split(","),
            "openai": os.getenv("OPENAI_API_KEYS", "").split(","),
            "gemini": os.getenv("GEMINI_API_KEYS", "").split(","),
        }
        self.current_index = {k: 0 for k in self.providers}

    def get_next_key(self, provider: str):
        keys = self.providers.get(provider, [])
        if not keys or keys == [""]:
            return None
        key = keys[self.current_index[provider] % len(keys)]
        self.current_index[provider] = (self.current_index[provider] + 1) % len(keys)
        return key.strip()

    async def query(self, prompt: str, provider: str = "grok"):
        key = self.get_next_key(provider)
        if not key:
            # Fallback to next provider
            for p in ["openai", "gemini", "grok"]:
                if p != provider:
                    key = self.get_next_key(p)
                    if key:
                        provider = p
                        break
        if not key:
            return "Error: No API keys available."

        # Placeholder - actual API calls would go here
        return f"Response from {provider} for: {prompt[:50]}..."
