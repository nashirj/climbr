# Climbr

A "staging" version of the app is available at https://climbr-stage.herokuapp.com and a "production" version is available at https://climbr-pro.herokuapp.com

This project is based off of the [palletsprojects Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/). The code was updated to use a Postgres database following this [real python tutorial](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)

---
## TODO
- show preview of route when hovering over link to details page: https://stackoverflow.com/questions/10769016/display-image-on-text-link-hover-css-only
- add profile view that shows all routes posted by user
- show only holds that are on current configuration of the wall
- implement filtering by route difficulty
- implement uploading image: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
- implement email verification: https://realpython.com/handling-email-confirmation-in-flask/
- get opencv working on heroku (https://stackoverflow.com/questions/49469764/how-to-use-opencv-with-heroku)
- add feature to upload/download route data
- update database model to have a parameter for the grade of the route
- add color coding for start holds
