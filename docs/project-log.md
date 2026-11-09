# Project Log

This log summarises development milestones, scope decisions and
verification. Earlier plans are distinguished from the current
implementation.

## Planning and Setup

- Selected Driveway as a car-shortlisting application.
- Reviewed the supplied project requirements and submission checklist.
- Created the Python virtual environment and Django project.
- Recorded dependencies in `requirements.txt`.
- Configured the secret key and DEBUG setting through environment variables.
- Excluded local environment files and the virtual environment from Git.
- Connected the repository to GitHub.
- Created a public project board for user stories and acceptance criteria.
- Prepared desktop and mobile wireframes using Lucidchart AI,
  then reviewed and adjusted the layouts.

### Initial Decisions

- Users add their own cars rather than choosing from a fixed catalogue.
- Uploaded photographs retain their original backgrounds.
- Manual entry and photograph uploads provide the core input method.
- Automatic listing imports were considered for the initial release.
- Personal driveway uploads and car-image placement were identified
  as future development.

## Car Model and Database

- Created the `cars` application and custom `Car` model.
- Linked each car to its owner through Django's user model.
- Added specifications, listing URL, photograph, notes and timestamps.
- Installed Pillow to support image validation.
- Created and applied database migrations.
- Added petrol plug-in hybrid as a fuel option through a further migration.
- Confirmed Django's system checks passed.

## Homepage, Accounts and Car Management

- Built the shared layout, homepage, account forms and shortlist.
- Implemented registration, login and POST-based logout.
- Added username display and feedback messages.
- Implemented frontend car creation, detail, editing and deletion pages.
- Added deletion confirmation.
- Restricted car queries to the signed-in owner.
- Manually tested account actions, car management and access restrictions.

A car card initially appeared to remain after deletion. The cause was
not established. Subsequent deployed deletion checks passed, and automated
tests confirmed that deletion removes the database record.

## Car Comparison

- Added the comparison view, route, template and selection controls.
- Corrected an initial missing-view error during development.
- Implemented comparison of two or three owned cars.
- Added server-side checks for invalid selections and unavailable cars.
- Verified valid comparisons and rejection of invalid selections.

## Deployment and Persistent Storage

- Configured Gunicorn, WhiteNoise and the Heroku deployment files.
- Connected the Heroku application to the GitHub repository.
- Configured PostgreSQL for production data.
- Configured Cloudinary for uploaded photographs.
- Stored production credentials in Heroku Config Vars.
- Deployed the application and tested its main user journeys.
- Confirmed that saved car details and photographs remained available
  after a Heroku restart.

## Scope Review

Automatic listing imports were deferred to prioritise a reliable,
tested release with accounts, private shortlists, car management
and comparison.

Photo sliders, driveway visualisation and registration-number lookup
also remain future features. The README and backlog distinguish
these plans from implemented functionality.

## JavaScript Enhancement

- Added an external comparison script loaded only on the shortlist page.
- Added a live selection counter and feedback for invalid submissions.
- Prevented selection of a fourth car.
- Used a polite live region and focusable feedback.
- Tested keyboard interaction.
- Confirmed that comparison still works through Django validation
  when JavaScript is disabled.
- Resolved a JSHint warning and obtained a clean validation result.

## Testing and Validation

- Added 14 automated Django tests with GitHub Copilot assistance.
- Reviewed tests covering car management, ownership restrictions,
  comparison selections and selected form validation.
- Ran the suite using in-memory SQLite and local file storage;
  all 14 tests passed.
- Performed HTML, CSS, Python and JavaScript validation.
- Corrected Python formatting issues and reran checks.
- Tested responsive layouts and user journeys in Chrome and Safari.
- Recorded homepage Lighthouse results:
  mobile 98/100/100/100 and desktop 100/100/100/100.
- Documented results, limitations and evidence in
  [testing.md](testing.md).

## Final Audit and Corrections

- Used Copilot to inspect application code, configuration and documentation.
- Identified an incorrect password-validator configuration introduced
  during line wrapping: trailing commas made validator names tuples.
- Corrected the configuration and verified that all four validators load.
- Moved SecurityMiddleware before WhiteNoise.
- Added production HTTPS redirection, proxy recognition and secure cookies.
- Reran Django's system check successfully.
- Reran all 14 automated tests successfully after the settings changes.
- Updated the documented test command to disable HTTPS redirection
  only within the isolated test process.
- Updated the README to reflect implemented features and future plans.
- Added the wireframe image and full-size link.
- Replaced the duplicated project-log content in the backlog with
  priorities and remaining tasks.

The automated suite does not cover registration form processing.
Registration therefore requires a fresh live check after deploying
the password-validator correction.

## Remaining Verification

- Deploy the latest settings corrections.
- Verify HTTPS redirection, registration, login and core actions
  on the final deployed version.
- Revalidate the updated shortlist HTML.
- Check documentation links, screenshot evidence and image credits.
- Review database documentation and setup instructions.
- Reconcile the project board with completed and deferred work.
- Complete final repository and submission checks.

## AI Use

- ChatGPT supported planning, implementation guidance, debugging,
  testing explanations and documentation.
- Lucidchart AI supported the initial wireframe layouts.
- GitHub Copilot assisted with automated tests, comparison JavaScript,
  formatting changes and the repository audit.

Generated changes were reviewed and checked through targeted commands,
automated tests and manual testing. The password-validator issue found
during final review demonstrated why passing style checks and a limited
test suite do not replace testing all affected user journeys.