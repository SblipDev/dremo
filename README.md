<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="http://dremo.sblip.dev">
    <img src="https://dremo.sblip.dev/images/logo.png" alt="Logo" width="200" height="200">
  </a>

  <h2 align="center">Dremo</h3>
    <h4 align="center">CURRENTLY IN DEVELOPMENT</h2>
  <p align="center">
    Dremo is a community app in which you can join several communities, post stuff you like, comment and just have fun!
    <br />
    <br />
    <a href="https://github.com/shaurya-blip/dremo/issues">Report Bug</a>
    ·
    <a href="https://github.com/shaurya-blip/dremo/issues">Request Feature</a>
  </p>
</p>

## Installation and Running the code.

#### Python side: 

use pip to install all the dependencies.

```
$ pip install -r requirements.txt
```

After the dependencies are installed, run the following commands. 

```
$ python3 manage.py migrate
$ python3 manage.py runserver
```

If the following commands execute without any problems, the backend server has started. Now keep the server running as we go to the javascript instructions.

#### Javascript Side

Go in the frontend/ directory of the repository using this command, 

```
$ cd frontend/
``` 

and to install all the dependencies, run this command ->

```
$ npm install
```

now we have to run the server ->

```
$ npm run serve
```

Please keep sure that both the servers are running, then open `http://localhost:8000` or `http://127.0.0.1:8000`. If its working, you will be able to see the home page.

## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Twitter - [@dremodev](https://twitter.com/dremodev) <br>
Project Link: [https://github.com/shaurya-blip/dremo/](https://github.com/shaurya-blip/dremo/) <br>
Website : [https://dremo.sblip.dev](https://dremo.sblip.dev) <br>
