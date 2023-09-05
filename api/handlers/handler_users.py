from api.models.model_users import User, session


def get_list_users():
    users = session.query(User).all()
    users_in_dictionary = []
    for user in users:
        data = {"id": user.id, "username": user.username, "email": user.email}
        users_in_dictionary.append(data)
    return users_in_dictionary


def get_user_by_id(user_id):
    user = session.query(User).filter(
        User.id == user_id
    ).first()

    if user:
        data = {"id": user.id, "username": user.username, "email": user.email}
        return data
    return {'message': 'not found'}


def create_user(new_user_data):
    new_user = User(
        username=new_user_data.username,
        email=new_user_data.email
    )
    session.add(new_user)
    session.commit()

    return {"message": f"User {new_user.username} created successfully"}


def update_user_by_id(user_id, new_data):
    user = session.query(User).filter(User.id == user_id).first()

    if user:
        user.username = new_data.username
        user.email = new_data.email
        session.commit()
        return {'message': f'User {user.id} updated successfully'}

    return {'message': 'User not found'}


def delete_user_by_id(user_id):
    user = session.query(User).filter(User.id == user_id).first()

    if user:
        session.delete(user)
        session.commit()
        return {'message': f'User {user.username} deleted successfully'}

    return {'message': 'User not found'}
