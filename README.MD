# what this project is about

This project is all about building a optimized file uploader. Rather than storing files on the database itself, we'll be using links to a storage bucket for downloading. This will make everything faster, smoother, and generally makes the most sense. We've chosen to use a PostgreSQL database for this project because it's the perfect choice for what we're trying to accomplish.

# challanges

creating the api from scratch
While I am no stranger to APIs, building one that's as optimized as we want it to be is definitely going to be a challenge. In particular, figuring out how to manage unique user IDs across a user base of 10,000+ people is going to be interesting. But hey, that's my job. This will be a fun project

# roadmap

1. ~~Create a basic CRUD app using Python.~~

2. create the front-end using vue
   - not started
3. connected cloud flare with api to uploaded files
   - not started
4. save file links to the db and redicred users to the bucket when they want to download file
   - not started
