import express from 'express';
import { engine } from 'express-handlebars';
import fetch from 'node-fetch';

const PORT = 3000;
const app = express();

app.use(express.urlencoded({ extended: true }));

app.engine('handlebars', engine());
app.set('view engine', 'handlebars');
app.set('views', './views/');

app.get('/', async (req, res) => {
    let CL = "No data yet";

    try {
        const controller = new AbortController();
        const timeout = setTimeout(() => controller.abort(), 5000);

        const response = await fetch("http://127.0.0.1:8000/api/data", { signal: controller.signal });
        clearTimeout(timeout);

        const data = await response.json();
        CL = data.message;
    } catch (err) {
        console.error("FastAPI fetch failed:", err);
    }

    res.render('index.handlebars', { test: CL });
});

app.listen(PORT, () => {
    console.log(`Express server running on port ${PORT}`);
});
