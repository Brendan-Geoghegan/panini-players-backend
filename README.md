# Panini-players (Backend)
## Project description
Backend repository for Panini Players' trading platform.
## Routes
| Method | Route | Description |
| ------ | ----- | ----------- |
| GET | / | 'Panini Players woooooooooop' |
| GET | /stickers/:code | Returns the sticker associated with code |
| POST | /stickers/:code | Adds sticker to a user's collection |
| PUT | /stickers/:code | Removes sticker from a user's collection |
| GET | /users/:username | Returns all data associated with user |
| GET | /friends/:id | Returns all data associated with a friend user |
| GET | /country/:code | Returns all data for each sticker associated with country code |
| GET | /users/:id/friends | Returns the user's friends list as a string |
| POST | /users/:id/friends | Adds user to desired user's friends list |
| GET | /users/:id/friends_list | Returns the user's friends list as a list of strings |
| GET | /users/:id/stickers | Returns the user's sticker collection as a dictionary with sticker code and sticker count |
| GET | /users/location/:location | Returns all users with entered location |
| POST | /location | Changes location associated with user account |
| POST | /register | Registers new user |
| POST | /login | Logs registered user in |
| GET | /logout | Logs user out |
## Installation & usage
- Hosted on [Render](https://panini-players-backend.onrender.com/)
## Technologies
- Flask
    - Flask-Mail
    - Flask-Login
    - Werkzeug
- SQLAlchemy
- Octoparse
## Process
- Started by using a web scraper (Octoparse) to get the required data for the app
- Cleaned scraped data to a suitable format for use in the app
- Created database schemas and models for tables
- Wrote basic routes required for planned funcitonality 
- Added authorisation using Flask-Login
- Added extra routes for added functionality 
- Hosted repo on Render
- Testing
## Screenshots

## Wins & Challenges
### Wins
- 86% test coverage!
### Challenges
- Testing auth (92% coverage achieved in the end)