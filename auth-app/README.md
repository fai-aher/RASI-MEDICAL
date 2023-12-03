# Auth App

Change to this directory:

```bash
$ cd RASI-MEDICAL/auth-app
```

Build docker image:

```bash
$ sudo docker build -t auth-app-image .
```

Run container:

```bash
$ sudo docker run -d -p 8080:8080 auth-app-image
```
