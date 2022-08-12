const url = require('url');

const myUrl = new URL('http://myURL.com:1000/hello.html?id=100&status=active');
const googleUrl = new URL('http://google.com');

// Serialized url
console.log(myUrl.href);
console.log(myUrl.toString());
console.log(googleUrl.href);

// host (root domain)
console.log(myUrl.host);
console.log(myUrl.hostname);
console.log(googleUrl.host);

// pathname
console.log(myUrl.pathname)
console.log(googleUrl.pathname)

// serialized query
console.log(myUrl.search);

// params object
// create object
console.log(myUrl.searchParams);

// add param
myUrl.searchParams.append('abc','123');
console.log(myUrl.searchParams);
console.log(myUrl.href);

// loop through params
myUrl.searchParams.forEach((value,name) => console.log(`${name}: ${value}`))

