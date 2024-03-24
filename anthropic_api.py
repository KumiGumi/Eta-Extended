python

import os
import anthropic

def generate_response(prompt, max_tokens=100):
	client = anthropic.Client(os.environ["ANTHROPIC_API_KEY"])
	response = client.completion(
		prompt=f"[anthropic.HUMAN_PROMPT] {prompt} {anthropic.AI_PROMPT}",
		stop sequences=[anthropic.HUMAN_PROMPT],
		model="claude-v1",
		max_tokens_to_sample=max_tokens,
	)
	return response.completion