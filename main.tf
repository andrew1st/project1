provider "aws" {
  region = var.aws_region
}

resource "aws_instance" "fastapi" {
  ami           = var.ami_id
  instance_type = var.instance_type

  user_data = <<-EOF
    #!/bin/bash
    apt update -y
    apt install -y docker.io
    git clone https://github.com/andrew1st/project1.git
    cd <your-repo>
    docker build -t fastapi-app .
    docker run -d -p 8000:8000 fastapi-app
  EOF

  tags = {
    Name = "FastAPI-Server"
  }
}