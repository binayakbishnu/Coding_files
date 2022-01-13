const mongoose = require('mongoose');

const ordersSchema = mongoose.Schema({
    orderId: [{
        type: String,
        required: true
    }],
    title: [{
        type: String,
        required: true
    }],
    price: [{
        type: String,
        required: true
    }]
});

const customerSchema = mongoose.Schema({
    name: {
        type: String,
        // required: true
    },
    email: {
        type: String,
        // required: true
    },
    date: {
        type: Date,
        default: Date.now
    },
    // order: ordersSchema
});

module.exports = mongoose.model('customer', customerSchema);