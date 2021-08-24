var express = require('express');
const fetch = require("node-fetch");
var router = express.Router();

/* GET home page. */
router.get('/', async function (req, res, next) {
    const fetch = require("node-fetch");
    const amount = 4

    // Setting the background
    // let sas = await fetch("https://api.waifu.pics/sfw/shinobu")
    let back_pic_url = 'https://i.waifu.pics/PGj1tg7.gif'//(await sas.json()).url

    let cats = []
    let posts = []

    for (let i = 0; i < amount; i++) {
        let res = await fetch("https://thatcopy.pw/catapi/rest/")
        let cat = await res.json()
        cats.push(cat.url)
    }

    let descriptions = await (await fetch('https://binaryjazz.us/wp-json/genrenator/v1/story/' + amount)).json()

    cats.forEach((cat, index) => {
        posts.push(
            {
                pic: cat,
                content: descriptions[index]
            }
        )
    })

    res.render('index', {
        posts: posts,
        img_url: back_pic_url
    })


});

module.exports = router;
