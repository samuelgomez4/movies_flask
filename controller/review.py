from application import app
from model.repository import ReviewRepository
from model.entity import Review

repository = ReviewRepository()


@app.route("/api/reviews/<movie_code>", methods=["GET"])
def list_reviews(movie_code):
    return repository.findByMovieCode(movie_code)


@app.route("/api/reviews/<review_id>", methods=["GET"])
def findById(review_id):
    return repository.findById(review_id)


@app.route("/api/reviews", methods=["POST"])
def create_review():
    review = Review()
    repository.insert(review)


@app.route("/api/reviews", methods=["PUT"])
def update_review():
    review = Review()
    repository.update(review)


@app.route("/api/reviews/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    return repository.delete(review_id)
