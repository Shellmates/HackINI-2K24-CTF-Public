const crypto = require("crypto")
const express = require("express")
const session = require("express-session")
const bodyParser = require("body-parser")
const puppeteer = require("puppeteer")
require('dotenv').config()


const app = express();
const secret = "DkwEH3xjAgiUqjg";
const adminPassword = "DkwEH3xjAgiUqjg";

// ##################
// # Middleware
// ##################

app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({
    secret,
    cookie: {
        httpOnly: false
    },
}))

const setUserRoleMiddleware = (req, res, next) => {
    if (req.query.admin == adminPassword) {
        req.session.userRole = 'admin';
    } else {
        if (req.session.userRole != 'admin') {
            req.session.userRole = 'user';
        }
    }
    next();
};

app.use(setUserRoleMiddleware);


// ##################
// # Index page
// ##################

app.use(express.static("public"))

// ##################
// # Routes
// ##################

const FLAG = process.env.FLAG || "shellmates{redacted}";

app.get("/flag", async (req, res) => {
    try {
        console.log(req.session.userRole);
        if (req.session.userRole == 'admin') {
            res.status(200).send(FLAG)
        } else {
            res.status(200).send("Nice try, but no flag for you.")
        }
    } catch(err) {
	    // console.log(err)
        res.status(400).send("Something went wrong! If you think this is an error on our site, contact an admin.")
    }

})

// ##################
// # Navigation engine
// ##################

app.post("/go_somewhere", async (req, res) => {
    try {
        const path = req.body.path;
        if(typeof path !== "string") return res.status(400).send("No path provided");

        const browser = await puppeteer.launch({
            headless: "new",
            args: ["--no-sandbox", "--disable-dev-shm-usage", "--disable-setuid-sandbox"],
        });

        const context = await browser.createIncognitoBrowserContext();
        const page = await context.newPage();
        await page.goto(`http://localhost:3000/?admin=${adminPassword}`);

        await page.goto(path);
        await browser.close();
        res.status(200).send("I went there, it's a regulat website, isn't it ? :3")
    } catch(err) {
	    // console.log(err)
        res.status(400).send("Something went wrong! If you think this is an error on our site, contact an admin.")
    }
})

app.listen(3000);
