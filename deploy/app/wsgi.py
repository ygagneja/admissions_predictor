from app.main import app
from app import load_model_and_scalers

if __name__ == "__main__":
    load_model_and_scalers()
    app.run()