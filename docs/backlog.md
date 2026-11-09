# Product Backlog

Driveway's release priorities use MoSCoW:
**Must Have**, **Should Have**, **Could Have** and
**Won't Have in this release**.

User stories and acceptance criteria are tracked on the
[GitHub project board](https://github.com/users/Jasmeen-13/projects/1).

## Implemented Features

| Priority | Feature | Status |
| --- | --- | --- |
| Must Have | User registration, login and logout | Implemented and tested |
| Must Have | Private shortlists with owner-restricted access | Implemented and tested |
| Must Have | Frontend create, read, update and delete functionality | Implemented and tested |
| Must Have | Deletion confirmation | Implemented and tested |
| Must Have | Server-side validation and feedback messages | Implemented and tested |
| Must Have | Heroku deployment with persistent database storage | Deployed and tested |
| Should Have | Manual photograph uploads with persistent storage | Implemented and tested |
| Should Have | Comparison of two or three owned cars | Implemented and tested |
| Should Have | Listing links and personal notes | Implemented |
| Should Have | Responsive layouts and keyboard-accessible controls | Implemented and manually tested |
| Should Have | JavaScript selection counter and comparison feedback | Implemented and tested |

## Remaining Submission Tasks

- [ ] Deploy the latest password-validator, middleware and HTTPS settings fixes.
- [ ] Verify registration, login, HTTPS redirection and core actions after deployment.
- [ ] Revalidate the updated shortlist HTML and update its evidence.
- [ ] Verify documentation links, screenshot files and image credits.
- [ ] Review database documentation and setup instructions.
- [ ] Update the project log and reconcile the GitHub board.
- [ ] Complete the final repository and submission checks.

## Deferred Features

The following items are **Won't Have in this release**.
Their priority for a future release will depend on feasibility
and user needs.

| Feature | Intended benefit |
| --- | --- |
| Import specifications and photographs from a single listing URL | Reduce manual entry |
| Multiple photographs per car | Show more detail about each vehicle |
| Smooth transitions between vehicles | Improve browsing and comparison |
| Scrolling exterior-to-interior galleries | Present available listing photographs in a guided sequence |
| Personal driveway photograph uploads | Let users visualise cars in their own space |
| Drag and resize a car image on the driveway | Give users control over image placement |
| Background removal and automatic placement | Improve driveway visualisation |
| Registration-number lookup | Populate supported vehicle specifications |

Automatic imports and vehicle lookup require investigation of suitable
data providers, permitted access and available information.
Manual entry and uploads would remain available as fallbacks.

## Scope Decision

Automatic photo import was considered during initial planning but
deferred to prioritise reliable car management, permissions, comparison,
deployment and testing. The current application uses manually entered
details and uploaded photographs.

The original visualisation concept remains a future direction rather
than an implemented feature.