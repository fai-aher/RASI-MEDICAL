# Auth App

Change to this directory:

```bash
$ cd RASI-MEDICAL/histories-app
```

Build docker image:

```bash
$ sudo docker build -t histories-app-image .
```

Run container:

```bash
$ sudo docker run -d -p 8080:8080 histories-app-image
```
