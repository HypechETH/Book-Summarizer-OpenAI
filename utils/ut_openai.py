import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt
client = openai.OpenAI()

@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def aichat(messages, openai_api_key):
    try:
        client = openai.OpenAI(api_key = openai_api_key)
        response = client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo-0125",
            # stream=True,
            # max_tokens=2000
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e



def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

# text = "test embedding"
# embeddings = get_embedding(text)