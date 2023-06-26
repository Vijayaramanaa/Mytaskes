let express  = require('express')
let path = require('path')
let app = express()
let port = 50000


app.use(express.static(path.join(__dirname,'/','build')))

app.get('/',(req,res)=>{
    // res.send('hi')
})

app.listen(port,(err)=>{
    if (err) console.log(err)
    console.log(`http://localhost:${port}`)
})