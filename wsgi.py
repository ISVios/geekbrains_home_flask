#!/usr/bin/env python
from blog.app import app


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
