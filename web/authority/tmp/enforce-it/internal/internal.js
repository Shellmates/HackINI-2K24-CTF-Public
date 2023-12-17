const express = require('express');
const dotenv = require('dotenv');

dotenv.config({path: '/server/.env'});

const app = express();

app.use(express.json());

// simple logging
app.use((req, res, next)=>{
    console.log('internal:', req.method, req.hostname, req.url);
    next()
});

app.get('/internal',(req, res)=>{
    res.status(200).send("That's the internal panel ... but no flags");
});


app.listen(process.env.INTERNAL_PORT, () => {
    console.log(`Internal admin panel running on port ${process.env.INTERNAL_PORT}`);
});   