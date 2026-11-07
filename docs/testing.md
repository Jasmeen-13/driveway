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

### Follow-up

A car card initially appeared to remain after deletion. It later
disappeared, but the cause was not established. Repeat this test
during final regression testing.

Direct unauthorised POST requests, automated tests and deployed-site
testing are still pending.