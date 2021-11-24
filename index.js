const express = require("express")
const app = express()

var link

app.get("/", (req, res) => {
	res.render("index.ejs", {
		link
	})
})

app.get("/ngrok", (req, res) => {
	link = req.query.link
	res.send("ok")
})

app.listen(process.env.PORT)
