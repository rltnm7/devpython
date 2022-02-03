from flask import jsonify, render_template
from configuration import host, port, app, debug
from response import UserResponse, UserDetailResponse
from service import UserService

service = UserService()

@app.route('/users')
def list_users():
    user_entities = service.find_all()
    user_responses = []
    for user_entity in user_entities:
        user_response = UserResponse(id=user_entity.id, username=user_entity.username)
        user_responses.append(user_response)

    return render_template("users.html", users=user_responses)

@app.route('/users/<username>')
def get_user(username):
    user_entity = service.find_by_username(username)
    user_response = UserDetailResponse(id=user_entity.id, username=user_entity.username,
        name=user_entity.name, birthday=user_entity.birthday, age=user_entity.age)

    return render_template("user_detail.html", user=user_response)

if __name__ == '__main__':
    app.run(host=host, port=port, debug=debug)
