# Testing

## Manual tests 

Tests performed locally using Django's development server.

| Test | Expected result | Result |
| --- | --- | --- |
| Register | Account created, user signed in, success message | Pass |
| Log out | Return home with logout message | Pass |
| Log in | Open shortlist with username and success message | Pass |
| Add car with photo | Saved details and photo displayed | Pass |
| Edit price | Updated price and success message displayed | Pass |
| Cancel deletion | Car remains saved | Pass |
| Confirm deletion | Car removed and success message displayed | Pass |
| Logged-out access to car details | Redirect to login | Pass |
| Second account shortlist | First account's cars are absent | Pass |
| Another user's detail, edit and delete URLs | Return 404 | Pass |
| Compare two owned cars | Selected cars appear side by side | Pass |
| Compare only one car | Show “Select two or three cars to compare.” | Pass |
| Live homepage | Page and styling load | Pass |
| Live registration | Account created and shortlist opens | Pass |
| Live car creation with photo | Car details and photo display | Pass |
| Persistence after Heroku restart | Saved car and photo remain available | Pass |
| Live edit | Updated price is saved and displayed | Pass |
| Live cancel deletion | Car remains saved | Pass |
| Live confirm deletion | Car card disappears from shortlist | Pass |
| Live compare two cars | Both cars and correct details appear | Pass |
| Live compare three cars | All three cars appear | Pass |
| Live compare one car | Selection validation message appears | Pass |
| Live compare no cars | Selection validation message appears | Pass |
| Live logged-out car access | Redirects to login | Pass |
| Live other user's car details | Returns 404 | Pass |
| Live account isolation | Other users' cars are absent from shortlist | Pass |
| Live other user's edit page | Returns 404 | Pass |
| Live other user's delete page | Returns 404 | Pass |
| Mobile layout | Pages remain readable, controls usable and comparison cards stack without horizontal overflow | Pass |


### Follow-up

A car card initially appeared to remain after deletion. It later disappeared, but the cause was not established. Repeat this test during final regression testing.

Direct unauthorised POST requests, automated tests and deployed-site testing are still pending.

## Automated tests

Created with GitHub Copilot assistance.

All 14 Django tests passed using an isolated in-memory SQLite database and local file storage. No system-check issues were reported.

Coverage includes car CRUD, ownership restrictions, logged-out redirects, comparison selections and form validation.
Registration/login, image uploads and CSRF protection are notcovered by this automated suite.

## HTML validation

The deployed homepage passed the Nu HTML Checker with no errors or warnings.

![Homepage HTML validation](screenshots/html-validation-home.png)

## JavaScript validation

compare.js passed JSHint with no warnings.
The selection counter, three-car limit, minimum selection message and keyboard controls were tested locally and passed.

![JavaScript validation](screenshots/javascript-validation.png)