const express = require('express');
const dotenv = require('dotenv');
const { curly } = require('node-libcurl');

dotenv.config({path: '/server/.env'});

const app = express();

app.use(express.json());
app.set('view engine', 'ejs');


// simple logging
app.use((req, res, next)=>{
    console.log('app:', req.method, req.hostname, req.url);
    next()
});

app.get('/',(req, res)=>{
    const home = '';
    res.status(200).render('home',{title:'Home page'});
});

app.get('/request',async (req, res)=>{
    if (req.header('X-Forwarded-With') != "127.0.0.1"){
        res.status(401).send('You don\'t have the permission to access this portion of the website')
    } else {
        if (req.query.endpoint){
            let url = req.query.endpoint;
            let legit_url = `127.0.0.1:${process.env.INTERNAL_PORT}/internal`;
            if(url.substring(0,4)=== "http" && url.substring(7,legit_url.length+7) == legit_url){
                const {statusCode, data, headers} = await curly.get(url);
                res.status(200).send(data.toString());
            } else {
                let endpoint = "Invalid URL";
                res.status(401).render('internal',{title: 'internal page',endpoint});
            }
        } else {
            let endpoint = "Submit a valid url";
            res.status(200).render('internal',{title: 'internal page', endpoint});
        }
    }
})

app.use((req, res)=>{
    res.redirect('/');
})

app.listen(process.env.EXTERNAL_PORT, () => {
    console.log(`Server running on port ${process.env.EXTERNAL_PORT}`);
});   