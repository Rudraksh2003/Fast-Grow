provider "aws" {
  region = "us-west-2"  # Change this to your desired AWS region
}

resource "aws_instance" "fast_grow" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 AMI (change as needed)
  instance_type = "t2.micro"
  key_name      = var.key_name

  security_groups = [aws_security_group.fast_grow_sg.name]

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo amazon-linux-extras install docker -y
              sudo service docker start
              sudo usermod -a -G docker ec2-user
              sudo chkconfig docker on
              sudo docker run -d -p 5000:5000 yourdockerusername/comment-backend:latest
              sudo docker run -d -p 5001:5001 rudrakshladdha/data-backend:latest
              EOF

  tags = {
    Name = "fast-grow-ec2"
  }
}

resource "aws_security_group" "fast_grow_sg" {
  name_prefix = "fast-grow-sg-"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5001
    to_port     = 5001
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

variable "key_name" {
  description = "Name of the SSH key pair"
  type        = string
}

output "instance_public_ip" {
  value = aws_instance.fast_grow.public_ip
}

output "instance_public_dns" {
  value = aws_instance.fast_grow.public_dns
}

