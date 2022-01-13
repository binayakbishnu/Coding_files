const express = require('express');
const app = express();

app.use(express.json());

const db = require('./db');

const PORT = 3000;

const customerRoutes = require('./routes/customer_routes');
app.use('/customer', customerRoutes);

app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`)
});