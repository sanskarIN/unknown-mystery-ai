"""Demonstrate a local request/response inference contract.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.serving import InferenceRequest, LocalEndpoint


endpoint = LocalEndpoint(lambda payload: {"label": "positive" if payload["score"] >= 0.5 else "negative"})
request = InferenceRequest(
    request_id="demo-001",
    model_version="classifier-1.0",
    payload={"score": 0.8},
)
response = endpoint.handle(request)
print(response)
