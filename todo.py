from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

TODO = {
    "Todo1": {
        "content":"Todo1",
        "action":"pending",
        "timestamp":get_timestamp(),
    },
    "Todo2": {
        "content":"Todo2",
        "action":"pending",
        "timestamp":get_timestamp()
    },
    "Todo3": {
        "content":"Todo3",
        "action":"pending",
        "timestamp":get_timestamp(),
    }
}

def read_all():
    return list(TODO.values())

def create(todo):
    content = todo.get("content")
    action = todo.get("action", "")

    if content and content not in TODO:
        TODO[content] = {
            "content": content,
            "action": action,
            "timestamp":get_timestamp(),
        }
        return TODO[content], 201
    else:
        abort(
            406, f"{content} already exists!!"
        )

def read_one(content):
    if content in TODO:
        return TODO[content]
    else:
        abort(
            404, f"{content} Not found!"
        )

def update(content, todo):
    if content in TODO:
        TODO[content]["action"] = todo.get("action", TODO[content]["action"])
        TODO[content]["timestamp"] = get_timestamp()
        return TODO[content]
    else:
        abort(
            404, f"{content} not found!"
        )

def delete(content):
    if content in TODO:
        del TODO[content]
        return make_response(
            f"{content} successfully deleted", 200
        )
    else:
        abort(
            404, f"{content} not found!!"
        )