const express = require('express');
const router = express.Router();

// import customerSchema from '../Models/customer_model.js';
const Customer = require('../Models/customer_model.js');

// save data in to database
router.post('/addCustomer', async (req, res) => {
    const customer = new Customer({
        name: req.body.name,
        email: req.body.email,
        // order: {
        //     orderId: req.body.order.orderId,
        //     title: req.body.order.title,
        //     price: req.body.order.price,
        // }
    });
    try {
        const savedCustomer = await customer.save();
        res.json(savedCustomer)
    } catch (err) {
        console.log(err);
    }
});

module.exports = router;