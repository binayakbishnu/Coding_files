const fs = require('fs');
const path = require('path');

// create folder
// /* async by default */
// fs.mkdir(path.join(__dirname, '/test'), {}, function (err) {
//     if (err) throw err;
//     console.log('Folder created');
// });


// create and write to file
//! need makedir too b4 making file
// fs.writeFile(
//     path.join(
//         __dirname,
//         '/test',
//         '/test.txt'
//     ),
//     '1',
//     function (err) {
//         if (err) throw err;
//         console.log('File created');
//     }
// );
//^ writeFile overwrites previous content
// fs.appendFile(
//     path.join(
//         __dirname,
//         '/test',
//         '/test.txt'
//     ),
//     '2',
//     function (err) {
//         if (err) throw err;
//         console.log('File created');
//     }
// );
//! doesn't work when append followed by append since async
//* make append into callback of writeFile
// fs.writeFile(
//     path.join(
//         __dirname,
//         '/test',
//         '/test.txt'
//     ),
//     '1',
//     function (err) {
//         if (err) throw err;
//         console.log('File created');
//         fs.appendFile(
//             path.join(
//                 __dirname,
//                 '/test',
//                 '/test.txt'
//             ),
//             '2',
//             function (err) {
//                 if (err) throw err;
//                 console.log('File created');
//             }
//         );
//     }
// );


// read from file
// fs.readFile(
//     path.join(
//         __dirname,
//         '/test',
//         'test.txt'
//     ),
//     'utf8',
//     function (err, data){
//         if (err) throw err;
//         console.log(data);
//     }
// );

// rename file
// fs.rename(
//     path.join(
//         __dirname,
//         '/test',
//         'test.txt'
//     ),
//     path.join(
//         __dirname,
//         '/test',
//         'test2.txt'
//     ),
//     function (err) {
//         if (err) throw err;
//         console.log('File renamed');
//     }
// );



