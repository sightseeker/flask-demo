# flask-demo
Python with Flask with Docker

# Run
```
docker-compose up
```

# Access API

```
# Register or Update User
curl -i -X 'PUT' -H 'Content-Type:application/json' -d '{
  "username": "sightseeker",
  "firstName": "Sight",
  "lastName": "Seeker",
  "email": "sightseeker@example.com",
  "password": "password",
  "phone": "0ABCDEFGHJ",
  "userStatus": 0
}' http://localhost:5000/v1/user/0

# Get User
curl -i http://localhost:5000/v1/user/0

# Delete User
curl -i -X 'DELETE' http://localhost:5000/v1/user/0
```
