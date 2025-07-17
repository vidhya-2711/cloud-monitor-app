from flask import Flask, render_template
import boto3

app = Flask(__name__)

# Initialize Boto3 clients
ec2 = boto3.client('ec2', region_name='us-east-1')
ecs = boto3.client('ecs', region_name='us-east-1')
lambda_client = boto3.client('lambda', region_name='us-east-1')
s3 = boto3.client('s3', region_name='us-east-1')

@app.route('/')
def dashboard():
    # EC2 instances
    ec2_response = ec2.describe_instances()
    instances = [inst for r in ec2_response['Reservations'] for inst in r['Instances']]

    # ECS Clusters and Services
    clusters = ecs.list_clusters()['clusterArns']
    ecs_data = []
    for cluster in clusters:
        services = ecs.list_services(cluster=cluster)['serviceArns']
        ecs_data.append({'cluster': cluster, 'services': services})

    # Lambda Functions
    lambdas = lambda_client.list_functions()['Functions']

    # S3 Buckets
    buckets = s3.list_buckets()['Buckets']

    return render_template("index.html", instances=instances, ecs_data=ecs_data, lambdas=lambdas, buckets=buckets)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
