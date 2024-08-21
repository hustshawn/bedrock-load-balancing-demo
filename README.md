# Bedrock LLM Load Balancing Demo

This project is to demo the load balancing with Litellm among different LLMs from Amazon Bedrock.


## Setup
```
pip install -r requirements.txt
```
Ensure you have at least one AWS_PROFILE set up. Refer to [here](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html) if you do not know what is AWS Profile.

Then you can set `AWS_PROFILE_A` and `AWS_PROFILE_B` accordingly as 
```
export AWS_PROFILE_A=my-profile
```

## Run
```
python main.py
```

example output
```
IIntialized router with Routing strategy: simple-shuffle

Routing fallbacks: None

Routing context window fallbacks: None

Router Redis Caching=None
{'id': 'chatcmpl-257ad25f-8e04-4002-a1dd-a399b2f858b5', 'choices': [{'finish_reason': 'stop', 'index': 0, 'message': {'content': "I'm doing well, thanks for asking! I'm Claude, an AI assistant created by Anthropic.", 'role': 'assistant', 'tool_calls': []}}], 'created': 1718690987, 'model': 'anthropic.claude-3-sonnet-20240229-v1:0', 'object': 'chat.completion', 'system_fingerprint': None, 'usage': {'prompt_tokens': 14, 'completion_tokens': 25, 'total_tokens': 39}}
{'id': 'chatcmpl-f54b70b6-0a3b-4808-969c-bf1fbfbb08e9', 'choices': [{'finish_reason': 'stop', 'index': 0, 'message': {'content': "I'm doing well, thanks for asking!", 'role': 'assistant', 'tool_calls': []}}], 'created': 1718690989, 'model': 'anthropic.claude-instant-v1', 'object': 'chat.completion', 'system_fingerprint': None, 'usage': {'prompt_tokens': 16, 'completion_tokens': 13, 'total_tokens': 29}}
{'id': 'chatcmpl-bdcbccc5-722a-4e72-8903-6b7c4ce7dac8', 'choices': [{'finish_reason': 'stop', 'index': 0, 'message': {'content': "I'm doing well, thanks for asking!", 'role': 'assistant', 'tool_calls': []}}], 'created': 1718690991, 'model': 'anthropic.claude-instant-v1', 'object': 'chat.completion', 'system_fingerprint': None, 'usage': {'prompt_tokens': 16, 'completion_tokens': 13, 'total_tokens': 29}}
{'id': 'chatcmpl-319cd0e0-3392-4e26-9795-683cbe6fbd3a', 'choices': [{'finish_reason': 'stop', 'index': 0, 'message': {'content': "I'm doing well, thanks for asking!", 'role': 'assistant', 'tool_calls': []}}], 'created': 1718690993, 'model': 'anthropic.claude-instant-v1', 'object': 'chat.completion', 'system_fingerprint': None, 'usage': {'prompt_tokens': 16, 'completion_tokens': 13, 'total_tokens': 29}}
{'id': 'chatcmpl-bcdf1d92-9cff-4f17-b8ae-397e927b7759', 'choices': [{'finish_reason': 'stop', 'index': 0, 'message': {'content': "I'm doing well, thanks for asking! As an AI assistant, I don't experience emotions in the same way humans do, but I'm functioning properly and ready to assist you with any questions or tasks you may have. How can I help you today?", 'role': 'assistant', 'tool_calls': []}}], 'created': 1718690995, 'model': 'anthropic.claude-3-haiku-20240307-v1:0', 'object': 'chat.completion', 'system_fingerprint': None, 'usage': {'prompt_tokens': 14, 'completion_tokens': 55, 'total_tokens': 69}}
```

As you can see, I choose to invoke bedrock 5 times from the provided models list, and output the response json from different models. 
