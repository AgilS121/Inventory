
from web import app


if __name__ == "__main__":
    app.secret_key= "@123}webinventory{/@#$"
    app.run(debug=True)
    