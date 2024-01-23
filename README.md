# car-recommendation-system

Content based recommendation system using word embeddings. Built with Django, Docker, uWSGI, NGINX, Terraform, and
GitHub workflows

# How to run it locally

1. This project uses docker. If you don't have it
   installed, [you can find it here](https://docs.docker.com/engine/install/).
2. Clone current repository.
3. Run migrations `docker-compose run recommendation-system-python ./manage.py migrate cars`. This migration will
   populate the csv `cars/migrations/car_data.csv` into your sqlite db `db.sqlite3`.
4. Bring the application up `docker-compose up`. This command will bring up the services in the `docker-compose.yaml`
   (Nginx and Python).
5. The recommendation system should be ready. You can use your browser to interact with it
   at `http://127.0.0.1/api/v1/cars/?make=Nissan&model=200SX&year=1997&msrp=Low&number_of_recommendations=5`

   The following GET parameters are required, and they need to exist in the db (and therefore in the csv):
    - make
    - model
    - year
    - msrp

   The GET parameter `number_of_recomendations` is optional, and is 5 by default.

# How to run it in AWS

1. [Create an AWS account](https://aws.amazon.com/free).
2. [Generate secrets](https://k21academy.com/amazon-web-services/create-access-and-secret-keys-in-aws/) to interact with
   your account from the outside. You will need this for Step 4.
3. Clone this repository and push it into your own repo.
4. Create 4 secrets in your GitHub repository. Navigate to your settings -> Secrets and variables -> Actions -> New
   repository
   secret:
    - AWS_ACCESS_KEY: Paste the generated access key from AWS.
    - AWS_PROFILE: Pick a name, in my case I used `terraform`.
    - AWS_REGION: Pick a region, in my case I picked `us-east-1`.
    - AWS_SECRET_ACCESS_KEY: Paste the generated secret key from AWS.
5. Run the deployment workflow `.github/workflows/recommendation_system.yml` by going to your repository actions
   section.
   Click on `Deploy Recommendation System`, then on `Run workflow` and pick the branch you want to deploy. This workflow
   will use terraform to create an EKS and ECR, it will build a docker image of the application and deploy it into the
   EKS cluster.
6. Once the deployment has finished, a new ALB should be created in your [AWS account](console.aws.amazon.com). You can
   find it by typing EC2 into the search bar. Once you are in the EC2 page, scroll down to `Load Balancers` section.
   Finally click on the created ALB to find the DNS name.
7. You can use the DNS of that ALB to access the application from your browser. You may need to paste that DNS into the
   `ALLOWED_HOSTS` here `recommendation_system/settings.py`.

# Notes

If you change the content of the db, you will need to generate the car embeddings again. You can achieve that by running
the command `docker-compose run recommendation-system-python ./manage.py model_generator_command`. The model and the
vectors will be generated inside the folder `cars/word_embedding_models`.