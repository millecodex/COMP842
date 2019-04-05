# Create an app with Blockstack
This is based on the "Hello Blockstack" tutorial written for OSX users. If you are using a mac/linux, the blockstack version will be better to follow: [Hello, Blockstack Tutorial](https://docs.blockstack.org/browser/hello-blockstack.html). For this I am using Windows 10 which should be compatible with the lab.

First we will install or verify npm which is the package manager for node.js. To check the version and find out if npm is installed, open a command prompt and type `npm -v` (version). Here I have version 6.4.1.

![windows commmand prompt](/images/blockstack/npm-v.PNG)

If you need to install it, head over to https://nodejs.org/en/, download and install node.js for Windows which comes with npm. Verify from the command prompt as above.

Next we will install some support packages.
1. Yeoman: `npm install -g yo`
2. Blockstack app generator: `npm install -g generator-blockstack`

## Generate an initial Blockstack application
Create a directory for the app (make directory)
`mkdir hello-decentralized-world`
Navigate there (change directory)
`cd hello-decentralized-world`
Start the app
`yo blockstack`

![blockstack generator](/images/blockstack/yoblockstack.PNG)

You may get some errors here, for example the package `node-gyp` does not support python 3.x. You can direct it to python 2.7 by `npm config set python /path/to/executable/python2.7`. Additionally, Windows build tools may need to be installed via `npm install --global windows-build-tools` using administrator access (may not work in the lab).






## Other links that may help
- [installing npm](https://www.npmjs.com/get-npm)
- [running a node app on windows](http://blog.gvm-it.eu/post/20404719601/getting-started-with-nodejs-on-windows)
- The elliptic curve package game me an error, [this page](https://github.com/cryptocoinjs/secp256k1-node#installation) helped resolve it on windows
