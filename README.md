# Puzzle Hunt Site

### Setup



### Todos
Tasks
- [ ] Add email sending (need to hook up Mailgun to custom DNS)
- [X] Add duplicate team name verification
- [X] Send out email on account creation
- [X] Split out scoring into new `team_scores` table
- [X] Add timestamp of last solve to `team_scores` table
- [X] Slack webhooks for signup, scoring, etc,
- [X] Enter answer in puzzle page and validate
- [X] Scoring for puzzles
- [X] Do not double count already solved puzzles
- [X] Correct answer for puzzles
- [X] Change team code generation to automatic 4 character random string?
- [X] Add duplicate team passcode screening
- [X] Be able to manually delete team
- [X] Be able to manually change email + score
- [X] Be able to manually set new passcode
- [X] Total solves out of attempts per puzzle in puzzles page
- [X] Impose character limit on team name
- [ ] Add forgot password button
- [ ] Add change password mechanism
- [X] Add login system
  - [X] Hide relevant content behind login flag
  - [X] Make registration take a password field
  - [X] Make answer submits reflect team score
- [X] Show a team page
- [X] Show which puzzles are solved on puzzles page
- [X] Add an option to sort by most solved
- [ ] More robust checking around if team names or usernames are the same
- [X] Store hashed version of password, not plaintext
- [X] Add favicon
- [ ] Add About Us page

Hosting
- [X] Get domain name
- [ ] Move Mailgun emails to DNS
- [ ] Host site on domain
