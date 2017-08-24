import connexion
import datetime
import logging

from connexion import NoContent

USERS = {}

def get_user(id):
    logging.info(id)
    logging.info(USERS)
    user = USERS.get(id)
    logging.info(user['created'])
    # logging
    return user or (NoContent, 404)

def put_user(id, user):
    exists = id in USERS
    user['id'] = id
    if exists:
        logging.info('Updating user %s..', id)
        user['updated'] = datetime.datetime.utcnow()
        USERS[id].update(user)
    else:
        logging.info('Creating user %s..', id)
        user['created'] = datetime.datetime.utcnow()
        USERS[id] = user
    return NoContent, (200 if exists else 201)

def delete_user(id):
    exists = id in USERS
    if exists:
        del USERS[id]
        return NoContent, 204
    return NoContent, 404

logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__, specification_dir='./swagger/')
app.add_api('swagger.yaml')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True);
