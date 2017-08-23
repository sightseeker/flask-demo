import connexion
import logging

from connexion import NoContent

USERS = {}

def get_user(id):
    logging.info(id)
    logging.info(USERS)
    user = USERS.get(id)
    logging.info(user)
    # logging
    return user or (NoContent, 404)

def post_user(user):
    id = user['id']
    exists = id in USERS
    if exists:
        logging.info('Duplicate existed id : %s', id)
        USERS[id].update(user)
        return NoContent, 409
    logging.info('Create user id : %s', id)
    USERS[id] = user
    logging.info(USERS[id])
    return USERS[id], 200

def put_user(id, user):
    return NoContent, 204

def delete_user(id):
    exists = id in USERS
    if exists:
        return NoContent, 404
    return NoContent, 204

logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__, specification_dir='./swagger/')
app.add_api('swagger.yaml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True);
