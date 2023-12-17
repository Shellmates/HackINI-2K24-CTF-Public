const express = require('express');
const dotenv = require('dotenv');

dotenv.config({path: '/server/.env'});

const app = express();

app.use(express.json());

// simple logging
app.use((req, res, next)=>{
    console.log('hidden:', req.method, req.hostname, req.url);
    next()
});

app.get('/flag',(req, res)=>{
    res.status(200).send(`Here is the flag ${process.env.FLAG}`);
});


app.listen(process.env.SUBINTERNAL_PORT, () => {
    console.log(`Internal admin panel running on port ${process.env.SUBINTERNAL_PORT}`);
});   