resource "aws_ecr_repository" "alloy" {
  name                 = var.repository_name
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = false
  }
}

resource "aws_ecr_lifecycle_policy" "expire_old_containers" {
  repository = aws_ecr_repository.alloy.name

  policy = <<EOF
{
    "rules": [
        {
            "rulePriority": 5,
            "description": "Keep last 100 images",
            "selection": {
                "tagStatus": "tagged",
                "tagPrefixList": ["${var.tag_prefix_list}"],
                "countType": "imageCountMoreThan",
                "countNumber": 100
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
EOF
}
