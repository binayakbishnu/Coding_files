const path = require('path');

// basename
// to get base file name
console.log(__filename);
console.log(path.basename(__filename));

// dirname
// to get directory name
console.log(__filename);
console.log(__dirname);
console.log(path.dirname(__filename));

// extname
// to get file extension
console.log(path.extname(__filename));

// parse
// create path object
console.log(path.parse(__filename)); /* now it returns an object */
console.log(path.parse(__filename).base); /* gives base field from the object */

//join
// concatenate paths
console.log(path.join(__dirname,'test','hello.html'));



