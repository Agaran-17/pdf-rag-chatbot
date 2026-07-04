import os

try:
    from dotenv import load_dotenv
except ImportError as e:
    raise ImportError(
        "python-dotenv package not installed. Install with `pip install python-dotenv`."
    ) from e

try:
    import google.generativeai as genai  # type: ignore[import]
except ImportError as e:
    raise ImportError(
        "google.generativeai package not installed. Install with `pip install google-generativeai`."
    ) from e

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

for model in genai.list_models():
    print("MODEL:", model.name)
    print("METHODS:", model.supported_generation_methods)
    print("-" * 50)