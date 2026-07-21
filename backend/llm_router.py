import os
from dotenv import load_dotenv
import httpx

load_dotenv()

class LLMRouter:
    def __init__(self):
        self.providers = {
            "grok": os.getenv("GROK_API_KEYS", "").split(","),
            "openai": os.getenv("OPENAI_API_KEYS", "").split(","),
            "gemini": os.getenv("GEMINI_API_KEYS", "").split(","),
        }
        self.current_index = {k: 0 for k in self.providers}

    def get_next_key(self, provider):
        keys = [k.strip() for k in self.providers.get(provider, []) if k.strip()]
        if not keys:
            return None, None
        idx = self.current_index[provider] % len(keys)
        self.current_index[provider] = (self.current_index[provider] + 1) % len(keys)
        return provider, keys[idx]

    async def query(self, prompt: str, provider: str = "grok"):
        for attempt in ["grok", "openai", "gemini"]:
            p, key = self.get_next_key(attempt)
            if not key:
                continue
            try:
                if p == "openai":
                    async with httpx.AsyncClient() as client:
                        resp = await client.post("https://api.openai.com/v1/chat/completions", 
                            headers={"Authorization": f"Bearer {key}"},
                            json={"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}]},
                            timeout=30)
                        return resp.json()["choices"][0]["message"]["content"]
                # Add similar for Grok and Gemini
                return f"[{p}] {prompt[:100]}... (implement full call)"
            except:
                continue
        return "All providers exhausted."
