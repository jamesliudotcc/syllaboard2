Running using Docker:

Edit `Dockerfile` to reflect where on your file system you put the repo. Then run these commands:

```shell
docker build -t syllaboard2-a .
docker run -it --rm --port 5000:5000 syllaboard2-a
```

How to get the Postgres running (not currently used):

```
docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=postgres postgres
```

Initialize the SQLite:

```
flask db init
```
Create the initial migration:
```
flask db migrate -m "users table" (if no migrations exist)
```
Run the migration:
```
flask db upgrade # <- Probably only do this step
```

Run the tests

```
pytest -W ignore::pytest.PytestDeprecationWarning
```

- [ ] App Architecture
  - [x] Blueprints set up
  - [x] JSON decorator set up
  - [x] Consider moving `app.py` to `app/__init__.py`
  - [x] Colocate models with blueprints
  - [x] Get rid of circular imports on init https://github.com/ltalirz/flask-sqlalchemy-circular-imports
  - [ ] Tighten up Docker user permissions
  - [ ] Write a Docker Compose file to get this working with Postgres.


- [ ] Models
  - [x] Create a design schematic
  - [x] Set up SQLalchemy
    - [x] Set up hashing: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
  - [x] Set up migrations
  - [x] For now, just use SQLite
  - [ ] Set up PostgreSQL or cloud Cockroach

- [ ] Auth
  - [x] Use Flask-JWT-Extended to implement JWT
  - [ ] Some auth routes scaffolded
    - [x] Me
    - [x] Login
    - [x] Signup
    - [ ] New PW
      - Must be logged in, must provide correct password.
      - Passwords match to be verified on front-end.
    - [x] Logout is on client side: delete the token.
  - [x] Auth model created

- [ ] Instructor
  - [ ] Assignment
  - [ ] Cohort
  - [ ] Deliverable

- [ ] Admin
  - [ ] Users
    - [ ] Create one time password
    - [ ] Create a celery task to wait 15 minutes and invalidate that pw
  - [x] Cohorts
    - [x] Create cohort
    - [x] Assign instructor to cohort
    - [x] Assign student to cohort

- [ ] Student
  - [ ] Deliverable
    - [ ] Get all deliverables
    - [ ] Update a deliverable
    - [ ] Get pending deliverables (wishlist)

- [ ] Organize these
  - [x] Cohort model created
  - [ ] Admins model created

- [ ] Cleanup
  - [ ] Import most things when `flask shell`
  - [ ] JSON for default errors instead of HTML

- [ ] Testing
  - [x] Have tests https://tavern.readthedocs.io/en/latest/examples.html
  - [ ] Write tests against other users.

- [ ] Deploy
  - [ ] Build to a Docker image
  - [ ] Run with Docker Compose using a Postgres

- [x] First user is always created admin. After, users can be made
  admin only by an admin. Duh.
- [ ] (/cohort GET) should be paginated.