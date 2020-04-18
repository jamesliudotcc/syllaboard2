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
flask db migrate -m "users table"
```
Run the migration:
```
flask db upgrade
```

- [ ] App Architecture
  - [x] Blueprints set up
  - [x] JSON decorator set up
  - [x] Consider moving `app.py` to `app/__init__.py`
  - [x] Colocate models with blueprints
  - [x] Get rid of circular imports on init https://github.com/ltalirz/flask-sqlalchemy-circular-imports


- [ ] Models
  - [x] Create a design schematic
  - [x] Set up SQLalchemy
    - [x] **NEXT** Set up hashing: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
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
    - [x] Logout is on client side: delete the token.
  - [ ] Auth model created

- [ ] Instructor
  - [ ] Assignment
  - [ ] Cohort
  - [ ] Deliverable

- [ ] Admin
  - [ ] Users
  - [ ] Cohorts

- [ ] Student
  - [ ] Deliverable
    - [ ] Get all deliverables
    - [ ] Update a deliverable
    - [ ] Get pending deliverables (wishlist)

- [ ] Organize these
  - [ ] Cohort model created
  - [ ] Admins model created

- [ ] Cleanup
  - [ ] Import most things when `flask shell`
  - [ ] JSON for default errors instead of HTML

- [ ] Testing
  - [ ] Have tests https://tavern.readthedocs.io/en/latest/examples.html
  - [ ] 

- [ ] Deploy
  - [ ] Build to a Docker image
  - [ ] Run with Docker Compose using a Postgres