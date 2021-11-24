const express = require("express")
const app = express()

app.get("/ngrok", (req, res) => {
	console.log(req.query.link)
	res.send("ok")
})

app.listen(9000)
