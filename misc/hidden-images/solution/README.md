# Solution
- Let's read the description carefully
  > In our organization we make strict rules about our repositories.
  > We are suspsecting that one of our developers isn't following rules.
  > Can you make sure of it?
- One of the key words is `repositories` in which we can think about `GitHub`, `GitLab`, `DockerHub` ... etc
- Taking in consideration the challenge name `Hidden Images` make us think about `DockerHub`
- Another key express is `one of our developers` which make us think about one of the authors
- The best one to start with is the author of the challenge `rx0f`
- By searching him on dockerhub, we'll find he has a suspicious image named `not-sus`
- We'll use `docker compose` to pull the image and run it
```yaml
version: '3.8'

services:
  server:
    build: .
    image: rx0f/not-sus
```
- Now we use docke to run the container
```bash
docker run -it rx0f/not-sus:latest sh
```
- Now we list the files inside the container
```bash
bin    dev    etc    flag   home   lib    media  mnt    opt    proc   root   run    sbin   srv    sys    tmp    usr    var
```
- If we try to read the flag file directly it displays unreadable text
- We try to run it now

# Flag
> shellmates{N0w_Y0u_Kn0W_4bOuT_d0cK3R_huB}