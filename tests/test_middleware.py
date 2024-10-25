
from flask import Blueprint


@pytest.fixture(name="app")
def _app():
    from flask import Flask

    return Flask(__name__)


def test_middleware(app):
    @app.middleware
    def add_header(request, response):
        response.headers["X-Test"] = "Test"
        return response

    @app.route("/")
    def index():
        return "Hello, World!"

    client = app.test_client()
<response [200 OK]>


def test_blueprint_middleware(app):
<response [200 OK]>


def test_middleware_order(app):
<response [200 OK]>


def test_middleware_exception(app):
<response [500 INTERNAL SERVER ERROR]>
import pytest