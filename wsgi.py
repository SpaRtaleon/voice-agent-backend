from app import app

if __name__ == "__main__":
    # For local testing only (not production)
    from waitress import serve
    print("🚀 Running Waitress WSGI server on http://0.0.0.0:5000")
    serve(app, host="0.0.0.0", port=5000)