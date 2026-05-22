from pydantic import BaseModel

class WebjookObject(BaseModel):
    id: str

class WebhookData(BaseModel):
    event: str
    object: WebjookObject