# Create an app with Blockstack
This is based on the "Hello Blockstack" tutorial written for OSX users. If you are using a mac/linux, the [blockstack version](https://docs.blockstack.org/browser/hello-blockstack.html) will be better to follow. For this I am using Windows 10 which ~~should~~ might be compatible with the lab.

First we will install or verify npm which is the package manager for node.js. To check the version and find out if npm is installed, open a command prompt and type `npm -v` (version). Here I have version 6.4.1.

![windows commmand prompt](/images/blockstack/npm-v.PNG)

If you need to install it, head over to https://nodejs.org/en/, download and install node.js for Windows which comes with npm. Verify from the command prompt as above.

Next we will install some support packages.
1. Yeoman: `npm install -g yo`
2. Blockstack app generator: `npm install -g generator-blockstack`

## Generate an initial Blockstack application
Create a new directory for the app (make directory)\
`C:\Users\Japple> mkdir hello-decentralized-world`\
Navigate there (change directory)\
`C:\Users\Japple> cd hello-decentralized-world`\
Start the app\
`C:\Users\Japple\hello-decentralized-world> yo blockstack`

![blockstack generator](/images/blockstack/yoblockstack.PNG)

Select `Y` to proceed. You may get some errors here. For example:
- the package `node-gyp` does not support python 3.x. You can direct it to python 2.7 by `npm config set python /path/to/executable/python2.7`. 
- Additionally, Windows build tools may need to be installed via `npm install --global windows-build-tools` (needs administrator access, may not work in the lab).

Once `yo blockstack` runs without any errors you will see: `found 0 vulnerabilities` and are ready.

Start the server by:\
`C:\Users\Japple\hello-decentralized-world> npm start`\
This will load in your browser, note the address is `http://localhost:5000`. You may be prompted to accept incoming connections.

![hello blockstack!](/images/blockstack/helloBlockstack.PNG)

Click sign in. You will be prompted to create a new ID. 

![createID](/images/blockstack/newID.PNG)

Select a username. A backup phrase will be emailed to you. Login with the new userID and leave the application running.

![nameless Person](/images/blockstack/nameless.PNG)

From this point on you can inspect some of the code and commit to a git repo by following the [blockstack version](https://docs.blockstack.org/browser/hello-blockstack.html#understand-the-generated-application-code).

The files `app.js` and `manifest.json` contain most of the logic for the app.

## Exercise
1. Now that you have a blockstack userID and the environment installed, try the [Todo List Application Tutorial](https://docs.blockstack.org/browser/todo-list.html).

## Other links that may help with installation
- [installing npm](https://www.npmjs.com/get-npm)
- [running a node app on windows](http://blog.gvm-it.eu/post/20404719601/getting-started-with-nodejs-on-windows)
- The elliptic curve package game me an error, [this page](https://github.com/cryptocoinjs/secp256k1-node#installation) helped resolve it on windows
