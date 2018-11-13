FROM docker-registry.iguokr.com/apps/battle-robot-app:latest
# Create the working directory (and set it as the working directory)
COPY . /app/
WORKDIR /app/

# Install the package dependencies (this step is separated
# from copying all the source code to avoid having to
# re-install all python packages defined in requirements.txt
# whenever any source code change is made)
RUN pip install --upgrade pip -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

RUN echo "Asia/Shanghai" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
