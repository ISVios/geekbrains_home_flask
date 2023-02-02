from flask_restful import Resource


class TagList(Resource):
    def get(self):
        return {"ok": "ok"}
