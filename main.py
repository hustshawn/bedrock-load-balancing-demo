import os
from litellm import Router
import asyncio

AWS_PROFILE_A = os.getenv("AWS_PROFILE_A", "us-east-1")
AWS_PROFILE_B = os.getenv("AWS_PROFILE_B", "account-b-us")

model_list = [
    {
        "model_name": "bedrock-claude",
        "litellm_params": {
            "model": "bedrock/anthropic.claude-instant-v1",
            "aws_profile_name": AWS_PROFILE_A,
            "timeout": 300,  # sets a 5 minute timeout
            "stream_timeout": 30,  # sets a 30s timeout for streaming calls
        },
    },
    {
        "model_name": "bedrock-claude",
        "litellm_params": {
            "model": "bedrock/anthropic.claude-3-haiku-20240307-v1:0",
            "aws_profile_name": AWS_PROFILE_B,
            "timeout": 300,  # sets a 5 minute timeout
            "stream_timeout": 30,  # sets a 30s timeout for streaming calls
        },
    },
    {
        "model_name": "bedrock-claude",
        "litellm_params": {
            "model": "bedrock/anthropic.claude-3-sonnet-20240229-v1:0",
            "aws_profile_name": AWS_PROFILE_B,
            "timeout": 300,  # sets a 5 minute timeout
            "stream_timeout": 30,  # sets a 30s timeout for streaming calls
        },
    },
]

# init router
router = Router(
    model_list=model_list,
    # more routing strategies refer to: https://docs.litellm.ai/docs/routing#advanced---routing-strategies
    routing_strategy="simple-shuffle",
)


async def router_acompletion(n):
    for i in range(n):
        response = await router.acompletion(
            model="bedrock-claude",
            messages=[{"role": "user", "content": "Hey, how's it going?"}],
        )
        print(response.model_dump())
    return response


asyncio.run(router_acompletion(5))
