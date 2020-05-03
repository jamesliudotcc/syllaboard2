# Readme

Since we will consuming this with fetch on the frontend, here is a little setup
for consuming the API using the command line.

## How to

Install with `yarn install`.

Run jay-repl with `npx jay`. That will put you in a node repl with top level
async.

Run the flask server. Duh.

```javascript
fetch = require('node-fetch') // 
resp = await fetch('http://localhost:5000/auth/login', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({email: "james@jamesliu.cc", password: "um..."})}) 
body = await resp.json() // You can only run .json() once, so save it. Coroutines. 🙄
body.access_token # And you get the accees token


post = (url, body) => (await fetch(url, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(body)}))

```