from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class URLRequest(BaseModel):
    url: str

class URLResponse(BaseModel):
    short_url: str

class URLAnalytics(BaseModel):
    short_code: str
    original_url: str
    visit_count: int
    created_at: datetime
    expires_at: Optional[datetime]