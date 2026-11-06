# Project Log

## 4 November 2026 — Planning and Setup

### Completed

- Reviewed the learning outcomes and pre-submission checklist.
- Selected Driveway as the project concept.
- Created the local project folder and Python virtual environment.
- Selected the virtual environment in VS Code.
- Installed Django 5.2.19 using Python 3.12.8.
- Created the Django project with the configuration package `config`.
- Recorded dependencies in requirements.txt.
- Moved the secret key into the ignored local env.py file.
- Configured DEBUG to read from the environment, defaulting to False.
- Ran the Django system check successfully.
- Initialised Git on the main branch.
- Verified Git ignores env.py and the virtual environment.

### Decisions

- Users choose and add their own cars; there is no fixed catalogue.
- Initial photographs retain their original backgrounds.
- Manual image upload is always available.
- Automatic photo import is requested for the initial release.
  Supported sources still need investigation.
- Personal driveway uploads and automatic car placement are future work.
- Planned work time is 6–7 hours Wednesday, 9 hours Thursday,
  9 hours Friday and some additional time Saturday.

### Next Steps

- Make the initial commit and connect the GitHub repository.
- Create a public project board with user stories and priorities.
- Prepare wireframes and the database design.
- Build the first working application features.
- Deploy an early version to Heroku.

### 6 November 2026 — Car model

- Created the cars app and Car model, linked to Django's user model.
- Added car details, an optional listing URL, photo and notes.
- Installed Pillow for image uploads.
- Applied database migrations successfully.
- Ran Django's system check: no issues reported.
- Frontend functionality is not yet implemented or tested.

### 6 November 2026 — Homepage and authentication

- Added car forms, views and URL routes.
- Built the shared layout, homepage, account forms and shortlist page.
- Manually verified registration, login, logout, redirects,
  username display and success messages: all passed.
- Car creation, editing and deletion still need templates and testing.