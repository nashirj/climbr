# Climbr

A "staging" version of the app is available at https://climbr-stage.herokuapp.com and a "production" version is available at https://climbr-pro.herokuapp.com

This project is based off of the [palletsprojects Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/). The code was updated to use a Postgres database following this [real python tutorial](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)

---
## TODO
- show preview of route when hovering over link to details page: https://stackoverflow.com/questions/10769016/display-image-on-text-link-hover-css-only
- overlay route onto image of wall with routes; draw bounding boxes around the holds that are part of specified route
    - ![](sample-route.JPG)
- add profile view that shows all routes posted by user
- make labels for checkboxes visible by pressing button
- show editable grid of holds on the update page
- show only holds that are on current configuration of the wall
- # TODO: display/save the old route when updating
- implement filtering by route difficulty
- implement uploading image: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
