from pydantic import BaseModel

class URLRequest(BaseModel):
    url: str

class URLResponse(BaseModel):
    short_url: str

class URLAnalytics(BaseModel):
    short_code: str
    original_url: str
    visit_count: int
