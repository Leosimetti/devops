## Best Practices
- Minimizing the image size
> Smaller images allow for download/build/deploy processes to be much faster.
> A good "tool" for trimming the image size is a properly configured `.dockerignore` file.
- Removing unnecessary dependencies 
> Unnecessary tools are both a waste and a security risk.
> For instance, having unneeded gcc installed can become a serious problem
> if someone gains access to the container shell.
- Using appropriate base images
> It is a good idea to use official images with needed tools installed
> rather than installing all of them necessary dependencies manually.
> Moreover, alpine/slim versions of images allow for great image size reduction.
- Reducing the number of layers and properly ordering them
> As each command creates a new layers - switching some commands around 
can reduce the build speed vi the layer caching.
> Additionally, combining some commands together (shell mainly) can reduce
> the total amount of layers.
- Using `docker scan` on created images.
> Security scan refers to the `Snyk` database in order to
> find known vulnerabilities in an image. 
- Decoupling applications
> ???

## References
1. [Building minimal docker containers](
https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3)
2. [Image-building best practices](
   https://docs.docker.com/get-started/09_image_best/)
3. [Dockerfile best practices](
   https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)