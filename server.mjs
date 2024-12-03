import express from "express";

const app = express();
const port = 1996;


// get query params and do string reverse
app.get("/", (req, res) => {
    const { str } = req.query;
    const reversedStr = str.split("").reverse().join("");
    res.send(reversedStr);
}
);


app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
    }
);