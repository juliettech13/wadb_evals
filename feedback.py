import os
import gradio as gr
from PIL import Image
import requests
import io
import json
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import random
import weave
from weave.flow.annotation_spec import AnnotationSpec
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

# initialize annotations for this project
annotation = weave.publish(AnnotationSpec(
    name="Doomer or Boomer",
    description="Doomer or Boomer or Neither",
    field_schema={ "type": "string", "enum": ["Doomer", "Boomer", "Neither"],},
), "doomer_or_boomer")

annotation_reason = weave.publish(AnnotationSpec(
    name="Reason",
    description="Reason why you chose this value, write before clicking.",
    field_schema={ "type": "string"},
), "reason")


# cell 2
# Load the Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('post.html.jinja')

# Load replies data
def load_replies():
    replies = []
    # Load replies from both files
    with open('data/replies_alpin.json', 'r') as f:
        data = json.load(f)
        replies.extend(data['thread']['replies'])
    with open('data/replies_daniel.json', 'r') as f:
        data = json.load(f)
        replies.extend(data['thread']['replies'])
    return replies


def get_random_post_and_analyze():
    replies = load_replies()
    post = random.choice(replies)

    # Format the post data for the template
    created_at = datetime.fromisoformat(post['post']['record']['createdAt'].replace('Z', '+00:00'))
    formatted_date = created_at.strftime('%b %d, %Y, %I:%M %p')

    # Convert AT URI to bsky.app URL
    at_uri = post['post']['uri']
    _, _, author_did, _, post_id = at_uri.split('/')
    post_url = f"https://bsky.app/profile/{post['post']['author']['handle']}/post/{post_id}"

    # Analyze the post
    # download the avatar and convert to PIL image
    avatar_uri = post['post']['author'].get('avatar')
    avatar_response = requests.get(avatar_uri)
    avatar_pil = Image.open(io.BytesIO(avatar_response.content))

    response_dict = analyze_post_sentiment(avatar_pil, post['post']['author']['displayName'], post['post']['record']['text'])
    analysis = response_dict['llm_classification']
    weave_call_id = response_dict['weave_call_id']

    post_data = {
        'author': post['post']['author'],
        'created_at': formatted_date,
        'text': post['post']['record']['text'],
        'like_count': post['post'].get('likeCount', 0),
        'repost_count': post['post'].get('repostCount', 0),
        'has_image': False,
        'post_url': post_url
    }

    return template.render(**post_data), analysis, weave_call_id, ''


def submit_feedback(user_selection, reason, weave_call_id):
    """
    Example function that could send user feedback (the user_selection)
    and the weave_call_id to your Weave (or any other) API.
    """
    call = weave_api.get_call(weave_call_id)

    if not call:
        raise Exception('No Weave call ID found, have you tried adding @weave.op to the analyze_post_sentiment function?')

    if reason:
        reason_resp = weave_api.server.feedback_create(
            {
            "project_id": weave_api._project_id(),
            "weave_ref": call.ref.uri(),
            "feedback_type": "wandb.annotation.reason",
            "annotation_ref": annotation_reason.uri(),
            "payload": {"value": reason},
            }
        )

    resp = weave_api.server.feedback_create(
        {
            "project_id": weave_api._project_id(),
            "weave_ref": call.ref.uri(),
            "feedback_type": "wandb.annotation.doomer_or_boomer",
            "annotation_ref": annotation.uri(),
            "payload": {"value": user_selection},
        }
    )

    # Ready to analyze the next post
    return get_random_post_and_analyze()
