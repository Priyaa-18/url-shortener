from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app import models, utils
from app.schemas import URLRequest, URLResponse

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to URL Shortener!"}

# Dependency: get DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten", response_model=URLResponse)
def shorten_url(request: URLRequest, db: Session = Depends(get_db)):
    short_code = utils.generate_short_code()
    new_url = models.URL(original_url=request.url, short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {"short_url": f"http://127.0.0.1:8000/{short_code}"}

@app.get("/{short_code}")
def redirect_url(short_code:str, db: Session = Depends(get_db)):
	url = db.query(models.URL).filter(models.URL.short_code == short_code).first()

	if url is None:
		raise HTTPException(status_code=404, detail="Short URL not found")


	# update click count
	url.visit_count += 1
	db.commit()

	return RedirectResponse(url.original_url)