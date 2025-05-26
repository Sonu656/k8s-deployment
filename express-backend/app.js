const express = require('express');
const cors = require('cors'); 

const app = express();
const PORT = 3000;

app.use(cors()); 

app.get('/api', (req, res) => {
  res.json({ message: 'Hello from Express Backend!' });
});

app.listen(PORT,'0.0.0.0',  () => {
  console.log(`Backend running on http://localhost:${PORT}`);
});

