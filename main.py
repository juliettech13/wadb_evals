from set_env import set_env
from dotenv import load_dotenv
import weave
from litellm import completion

load_dotenv()
set_env("WANDB_API_KEY")
set_env("OPENAI_API_KEY")

# initialize weave
weave_api = weave.init('evals-workshop')

# Initialize our LLM client


model = "openai/gpt-4o"

@weave.op
def analyze_post_sentiment(avatar, displayName, text):
    # Prompt for OpenAI to analyze the sentiment

    prompt = f"""Analyze the following Bluesky post and determine if the author is a:
    - DOOMER (someone who hates AI and uses derogatory language)
    - BOOMER (someone who doesn't understand AI and asks to remove their data)
    - NEITHER (neutral or positive response)

    Post: {displayName}: "{text}"

    Respond with just one word (DOOMER, BOOMER, or NEITHER) followed by a brief explanation.
    """

    response = completion(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    try:
        current_call = weave.require_current_call()
        weave_call_id = current_call.id
    except:
        weave_call_id = None

    return {
        "llm_classification": response.choices[0].message.content,
        "weave_call_id": weave_call_id
    }

# Lets test this out without tracing first
response_dict = analyze_post_sentiment("","Thomas","I fear that AI is Skynet")
print(response_dict)


