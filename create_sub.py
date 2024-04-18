from google.cloud import pubsub_v1

# Set your Google Cloud project ID
project_id = "cloud-kumari-kumari-400603"

# Set the topic name and subscription name
topic_name = "sample"
subscription_name = "sample-sub"

# Create a subscriber client
subscriber = pubsub_v1.SubscriberClient()

# Get the fully qualified topic path
topic_path = subscriber.topic_path(project_id, topic_name)

# Create a subscription to the topic
subscription_path = subscriber.subscription_path(project_id, subscription_name)
subscription = subscriber.create_subscription(request={"name": subscription_path, "topic": topic_path})

print(f"Subscription '{subscription_path}' has been created for topic '{topic_path}'.")
