from fastapi import FastAPI

tags_metadata = [
    {"name": "Gem Grabber", "description": "This contains all the Gem Grabber APIs"},
]


app = FastAPI(
    title="Gem Grabber APIs",
    description="This contains the documentation of all the Gem Grabber APIs.",
)

@app.get(
    "/games/"
)
def fetch_games():
    return [{'id': 1, 'player': 'karunasolanki','score':10},
            {'id': 2, 'player': 'karunasolanki', 'score':20}]
