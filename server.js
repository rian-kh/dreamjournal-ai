const express = require('express');
const app = express();
const port = 3000; 
const ipv4 = "your-ipv4"

app.get('/', (req, res) => {
    console.log(`${req.method} request: `, req.headers)
    res.send("response")
});

app.listen(port, ipv4, () => {
  console.log(`API server listening at ${ipv4}:${port}`);
});

